# Global Data Analytics & Business Intelligence Portfolio

### End-to-End Data Analytics, Business Intelligence & Predictive Modeling

Welcome to my central data analytics portfolio.

This repository showcases end-to-end analytical projects covering **data cleaning and ETL, business intelligence, statistical analysis, predictive modeling, customer analytics, and interactive dashboards**.

My approach focuses on turning raw and often messy data into **reliable analytical datasets, structured models, and business-ready insights**.

Projects combine reproducible Python workflows with SQL, Power BI, DAX, statistical analysis, and machine learning, following the **CRISP-DM framework** where appropriate.

---

## 🚀 Featured Portfolio Projects

### 1. Online Retail Sales Analytics: Data Wrangling & Power BI Dashboard

**Domain:** E-Commerce & Global Retail Operations
**Dataset:** 805K+ transactional records

**Objective:** Transform a large transactional dataset into a reliable analytical model and executive reporting system for monitoring revenue, products, customers, and markets.

* **Data Pipeline:** Python/Pandas ETL for cleaning transactional data, handling cancelled invoices, managing missing customer records, and standardizing numeric data.
* **Data Modeling:** Designed a Star Schema with a dedicated Calendar dimension and structured fact/dimension relationships.
* **BI Development:** Built Power BI measures using DAX, including dynamic `DIVIDE()` and `BLANK()` logic for robust KPI calculations.
* **Dashboard:** Developed a 3-page executive reporting suite covering revenue trends, product performance, customer behavior, and market performance.
* **Business Metrics:** Revenue, orders, customer retention, average order value, product performance, and Month-over-Month trends.
* **Scale:** 805K+ transactional records, approximately $18M in revenue, and 37K orders.

**Tech Stack:** `Python` `Pandas` `Power BI` `DAX` `Star Schema` `ETL` `Data Wrangling` `UI/UX`

---

### 2. Predictive Sales Forecasting & Supply Chain Analysis

**Domain:** Retail Logistics & Inventory Planning

**Objective:** Analyze historical sales patterns and build a predictive model to estimate future demand and support inventory planning.

* **Model:** Multivariate Linear Regression using Ordinary Least Squares.
* **Analysis:** Investigated relationships between sales, marketing activity, pricing, and seasonal patterns.
* **Model Evaluation:** Achieved an **R² of 0.960** with a **Mean Absolute Error (MAE) of 98.76 units**.
* **Business Application:** Used predictive results to support demand planning and inventory-related decision making.

**Tech Stack:** `Python` `Pandas` `Scikit-Learn` `Linear Regression` `Correlation Analysis` `Demand Forecasting`

---

### 3. Donor Behavior Analysis & Campaign Impact Assessment

**Domain:** Non-Profit Fundraising & Campaign Performance

**Objective:** Analyze donor behavior before and after a campaign launch and provide an interactive tool for exploring campaign performance.

* Audited transactional donation data and addressed temporal and data-quality issues.
* Compared donor behavior before and after the June 2026 campaign.
* Analyzed acquisition and retention patterns across donor segments.
* Built and deployed an interactive Streamlit dashboard for dynamic exploration.
* Identified measurable changes in channel performance following the campaign period.

**Tech Stack:** `Python` `Pandas` `Streamlit` `Data Cleaning` `Cohort Analysis` `Interactive Visualization`

**Live App:**
https://nini-donor-analytics-dashboard.streamlit.app/

---

### 4. Customer Segmentation via RFM Behavioral Clustering

**Domain:** E-Commerce & Customer Analytics

**Objective:** Segment customers according to purchasing behavior to support differentiated retention and engagement strategies.

* Built RFM features based on **Recency, Frequency, and Monetary Value**.
* Standardized features using `StandardScaler`.
* Applied K-Means clustering to identify behavioral customer groups.
* Evaluated candidate cluster configurations using the **Elbow Method** and **Silhouette Coefficient**.
* Identified three main customer lifecycle segments, including high-value, recent, and at-risk customers.

**Tech Stack:** `Python` `Pandas` `Scikit-Learn` `K-Means` `RFM Analysis` `Customer Segmentation`

---

### 5. Financial Credit Risk Analytics & Multi-Model Benchmarking

**Domain:** Financial Risk Management
**Dataset:** Taiwan Credit Dataset, 30,000 records

**Objective:** Compare classification models for predicting credit default risk while accounting for class imbalance.

* Compared Logistic Regression, Decision Tree, and Random Forest models.
* Addressed class imbalance using cost-sensitive learning with `class_weight='balanced'`.
* Engineered financial features including `UTILIZATION_RATE`.
* Evaluated model performance using ROC-AUC and classification metrics.
* Random Forest achieved the highest ROC-AUC among the evaluated models at **0.761**.

**Tech Stack:** `Python` `Scikit-Learn` `Random Forest` `Logistic Regression` `Decision Trees` `Feature Engineering` `ROC-AUC`

---

### 6. Healthcare Churn Predictive Modeling & Patient Retention

**Domain:** Private Healthcare Insurance & Customer Retention

**Objective:** Identify patterns associated with customer churn and evaluate a predictive classification approach.

* Built a Random Forest classification model using a simulated healthcare customer dataset.
* Used stratified train/test splitting and class balancing techniques.
* Evaluated performance using classification metrics and Precision-Recall analysis.
* Examined feature importance to identify variables associated with predicted churn.
* The analysis highlighted customer service interactions as an important predictive variable within the simulated dataset.

**Tech Stack:** `Python` `Pandas` `Scikit-Learn` `Random Forest` `Precision-Recall` `Feature Importance`

---

### 7. SpaceX Falcon 9 First-Stage Landing Prediction

**Domain:** Aerospace & Predictive Analytics
**Project:** IBM Data Science Capstone

**Objective:** Build a machine learning pipeline to predict whether a Falcon 9 first stage would successfully land.

* Collected data through REST APIs and web scraping with `BeautifulSoup`.
* Cleaned and transformed launch data for analysis.
* Performed exploratory and geospatial analysis using `Folium`.
* Compared multiple classification algorithms.
* Tuned model hyperparameters using `GridSearchCV`.

**Tech Stack:** `Python` `REST APIs` `BeautifulSoup` `Folium` `Scikit-Learn` `GridSearchCV` `Classification`

**Repository:**
https://github.com/NiNaCocaZero/SpaceX-Falcon9-Predictive-Analysis

---

## 🛠️ Technical Stack & Tooling

### Data Analysis & Programming

* Python
* Pandas
* NumPy
* SQL
* Scikit-Learn
* SciPy

### Business Intelligence & Visualization

* Power BI
* DAX
* Star Schema Modeling
* Streamlit
* Matplotlib
* Seaborn
* Plotly
* Folium

### Data Preparation & ETL

* Data Cleaning
* Automated Python ETL Workflows
* Feature Engineering
* REST APIs
* Web Scraping
* BeautifulSoup

### Analytical Methods

* CRISP-DM
* Statistical Analysis
* Hypothesis Testing
* Time-Series Analysis
* Supervised Machine Learning
* Unsupervised Machine Learning
* Customer Segmentation
* Predictive Modeling

---

## 📫 Professional Engagements

Available for **Data Analyst, Business Intelligence, dashboard development, data cleaning, ETL, and analytical projects**.

I am also expanding my expertise in **Data Engineering**, with a focus on data pipelines, relational databases, and cloud-based data platforms.

**Upwork:**
https://www.upwork.com/freelancers/ninidata

**GitHub:**
https://github.com/NiNaCocaZero
