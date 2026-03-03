import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import urllib.request
import os

# Page config
st.set_page_config(page_title="E-Commerce Analytics", layout="wide")

# Download data
@st.cache_data
def load_data():
    try:
        os.makedirs('data', exist_ok=True)
        base_url = "https://raw.githubusercontent.com/olist/work-at-olist-data/master/datasets/"
        files = ['olist_customers_dataset.csv', 'olist_orders_dataset.csv', 
                 'olist_order_items_dataset.csv', 'olist_products_dataset.csv',
                 'olist_sellers_dataset.csv', 'product_category_name_translation.csv']
        
        for file in files:
            filepath = f'data/{file}'
            if not os.path.exists(filepath):
                urllib.request.urlretrieve(base_url + file, filepath)
        
        # Load data
        customers = pd.read_csv('data/olist_customers_dataset.csv')
        orders = pd.read_csv('data/olist_orders_dataset.csv')
        order_items = pd.read_csv('data/olist_order_items_dataset.csv')
        products = pd.read_csv('data/olist_products_dataset.csv')
        category_translation = pd.read_csv('data/product_category_name_translation.csv')
        
        # Clean data
        orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])
        orders['purchase_year_month'] = orders['order_purchase_timestamp'].dt.to_period('M').astype(str)
        order_items['total_value'] = order_items['price'] + order_items['freight_value']
        
        # Add categories
        products = products.merge(category_translation, on='product_category_name', how='left')
        products['product_category_name_english'] = products['product_category_name_english'].fillna(products['product_category_name'])
        order_items = order_items.merge(products[['product_id', 'product_category_name_english']], on='product_id', how='left')
        order_items.rename(columns={'product_category_name_english': 'category'}, inplace=True)
        
        # Handle missing delivery dates
        orders['order_delivered_customer_date'] = pd.to_datetime(orders['order_delivered_customer_date'], errors='coerce')
        orders['order_estimated_delivery_date'] = pd.to_datetime(orders['order_estimated_delivery_date'], errors='coerce')
        
        return orders, order_items, customers
    
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        raise e

# Load data with spinner
with st.spinner('Loading data... Please wait (30-60 seconds)'):
    orders, order_items, customers = load_data()

# Dashboard
st.title("🛒 E-Commerce Sales Analytics Dashboard")

# KPIs
col1, col2, col3, col4 = st.columns(4)
total_revenue = order_items['total_value'].sum()
total_orders = orders['order_id'].nunique()
total_customers = orders['customer_id'].nunique()
avg_order_value = total_revenue / total_orders if total_orders > 0 else 0

col1.metric("Total Revenue", f"R$ {total_revenue:,.0f}")
col2.metric("Total Orders", f"{total_orders:,}")
col3.metric("Customers", f"{total_customers:,}")
col4.metric("Avg Order Value", f"R$ {avg_order_value:.2f}")

st.markdown("---")

# Charts row 1
col1, col2 = st.columns(2)

# Monthly Revenue
try:
    monthly = orders.merge(order_items[['order_id', 'total_value']], on='order_id')
    monthly_revenue = monthly.groupby('purchase_year_month')['total_value'].sum().reset_index()

    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(
        x=monthly_revenue['purchase_year_month'],
        y=monthly_revenue['total_value'],
        mode='lines+markers',
        fill='tozeroy',
        name='Revenue'
    ))
    fig1.update_layout(title='Monthly Revenue Trend', xaxis_title='Month', yaxis_title='Revenue (R$)')
    col1.plotly_chart(fig1, use_container_width=True)
except Exception as e:
    col1.error(f"Revenue chart error: {str(e)}")

# Top Categories
try:
    top_cat = order_items.groupby('category')['total_value'].sum().reset_index().sort_values('total_value', ascending=False).head(10)
    fig2 = px.bar(top_cat, x='category', y='total_value', title='Top 10 Categories by Revenue', color='total_value')
    col2.plotly_chart(fig2, use_container_width=True)
except Exception as e:
    col2.error(f"Category chart error: {str(e)}")

# Charts row 2
col3, col4 = st.columns(2)

# Delivery Performance
try:
    # Only calculate for delivered orders with valid dates
    delivered_orders = orders[
        (orders['order_status'] == 'delivered') & 
        (orders['order_delivered_customer_date'].notna())
    ].copy()
    
    if len(delivered_orders) > 0:
        delivered_orders['delivery_days'] = (
            delivered_orders['order_delivered_customer_date'] - 
            pd.to_datetime(delivered_orders['order_purchase_timestamp'])
        ).dt.days
        
        delivery_state = delivered_orders.merge(customers, on='customer_id').groupby('customer_state')['delivery_days'].mean().reset_index()
        fig3 = px.bar(delivery_state, x='customer_state', y='delivery_days', 
                      title='Avg Delivery Days by State', color='delivery_days')
        col3.plotly_chart(fig3, use_container_width=True)
    else:
        col3.info("No delivery data available")
except Exception as e:
    col3.error(f"Delivery chart error: {str(e)}")

# Order Value Distribution
try:
    payment_data = order_items.groupby('order_id')['total_value'].sum().reset_index()
    payment_data['tier'] = pd.cut(payment_data['total_value'], 
                                  bins=[0, 100, 500, 1000, float('inf')], 
                                  labels=['Low', 'Medium', 'High', 'Premium'])
    payment_dist = payment_data['tier'].value_counts().reset_index()
    payment_dist.columns = ['tier', 'count']
    fig4 = px.pie(payment_dist, values='count', names='tier', title='Order Value Distribution')
    col4.plotly_chart(fig4, use_container_width=True)
except Exception as e:
    col4.error(f"Distribution chart error: {str(e)}")

st.markdown("---")
st.caption("Built with Streamlit | Data: Brazilian E-Commerce Dataset")
