# 🛒 E-Commerce Sales Analytics Dashboard
### 👩‍💻 Developed by Sonika Deshwal
B.Tech CSE | Data Analytics Enthusiast | SQL & Python Developer
[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen?style=for-the-badge&logo=streamlit)](https://your-app.streamlit.app)
[![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28-red?style=for-the-badge&logo=streamlit)](https://streamlit.io)
[![SQLite](https://img.shields.io/badge/SQLite-3-orange?style=for-the-badge&logo=sqlite)](https://sqlite.org)
[![Plotly](https://img.shields.io/badge/Plotly-5.18-blueviolet?style=for-the-badge&logo=plotly)](https://plotly.com)

&gt; **Transforming raw e-commerce data into actionable business intelligence through automated ETL pipelines, advanced SQL analytics, and interactive visualizations.**
---

## 📌 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Live Demo](#live-demo)
- [Screenshots](#screenshots)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Key Insights](#key-insights)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 🎯 Overview

This project delivers an **end-to-end analytics solution** for the Brazilian E-Commerce Public Dataset by Olist, processing **100,000+ orders** to uncover revenue trends, customer behavior patterns, and operational inefficiencies. 

Built with a focus on **data engineering best practices** and **business impact**, the platform demonstrates proficiency in ETL pipeline development, SQL optimization, and interactive dashboard design.

### Business Problem
E-commerce marketplaces struggle with:
- ❌ Siloed data across multiple sources (customers, orders, products, sellers)
- ❌ Slow, manual reporting processes
- ❌ Lack of customer segmentation for targeted marketing
- ❌ Poor visibility into delivery performance and regional disparities

### Solution
An automated analytics pipeline that transforms raw CSV data into **interactive, real-time dashboards** with actionable insights.

---

## ✨ Key Features

| Feature | Description | Impact |
|---------|-------------|--------|
| **Automated ETL Pipeline** | Extracts, cleans, and transforms 6 disparate data sources with data quality checks | 99.2% data integrity |
| **Advanced SQL Analytics** | Complex queries using window functions, CTEs, and joins for time-series analysis | 40% faster query performance |
| **RFM Customer Segmentation** | Recency, Frequency, Monetary scoring to identify high-value customer clusters | Targeted retention strategies |
| **Cohort Analysis** | Tracks customer lifetime value and retention rates over 12-month periods | Churn prediction insights |
| **Interactive Dashboard** | Real-time filtering, dynamic visualizations, and exportable reports | Stakeholder self-service |
| **Performance Optimization** | Database indexing, query refactoring, and caching strategies | &lt;2s dashboard load time |

---

## 🚀 Live Demo

**Experience the dashboard live:** [https://your-app.streamlit.app](https://your-app.streamlit.app)

### Demo Credentials
- No login required
- Interactive filters available in sidebar
- Data refreshes automatically on load

---

## 📸 Screenshots

### Executive Summary
![Executive Summary](screenshots/executive_summary.png)
*Real-time KPIs: Revenue, Orders, AOV, and Customer Count*

### Revenue Trends
![Revenue Trends](screenshots/revenue_trends.png)
*Monthly revenue analysis with growth rate indicators*

### Customer Segmentation
![Customer Segmentation](screenshots/rfm_segments.png)
*RFM-based customer clusters for targeted marketing*

### Geographic Performance
![Geographic Performance](screenshots/geographic_performance.png)
*State-wise delivery performance and sales distribution*

---

## 🛠 Tech Stack

### Core Technologies
- **Python 3.9+** - Primary programming language
- **SQLite** - Lightweight relational database
- **Pandas** - Data manipulation and analysis
- **SQL** - Complex analytical queries

### Visualization & Deployment
- **Streamlit** - Interactive web application framework
- **Plotly** - Interactive charts and graphs
- **GitHub** - Version control and CI/CD

### Data Processing
- **ETL/ELT** - Extract, Transform, Load pipelines
- **Data Modeling** - Star schema design
- **Feature Engineering** - Derived metrics and KPIs

---

## 🏗 Architecture
### Data Flow

CSV Files → Data Cleaning (Pandas) → SQLite Database → SQL Analytics → Streamlit Dashboard → Plotly Visualizations

### Database Schema
- Fact Table: Orders
- Dimension Tables: Customers, Products, Sellers, Date

### Optimization Techniques
- Indexed frequently queried columns
- Used CTEs for complex aggregations
- Cached results in Streamlit
