# Global Data Analytics & Business Intelligence Portfolio
### Production-Grade Machine Learning Pipelines, Automated ETL & Executive Dashboards

Welcome to my central analytics repository. This portfolio demonstrates the design and deployment of end-to-end analytical systems: from raw transactional data wrangling and statistical modeling to interactive executive dashboards and supervised machine learning architectures.

Every project follows the **CRISP-DM framework**, emphasizing data integrity, reproducible code architectures, and high-impact business decision support.

---

## 🚀 Featured Portfolio Projects

### 1. Online Retail Sales Analytics: Data Wrangling & Power BI Dashboard
* **Domain:** E-Commerce & Global Retail Operations (805K+ Transactional Records)
* **Architecture:** Decoupled Pipeline (Python Back-End ETL + Power BI Front-End Modeling)
* **Technical Highlights:** Built an automated Pandas ETL script to clean cancelled orders, handle null customer records, and standardize float precisions. Implemented a Star Schema data model with an isolated `Calendario` dimension and engineered resilient DAX measures with dynamic `BLANK()` and `DIVIDE()` logic to prevent filter breakage.
* **Business Outcome:** Delivered an executive 3-page reporting suite tracking Total Revenue ($18M), Orders (37K), and Retention (72%) with responsive tooltips and dynamic Month-over-Month (MoM%) performance indicators.
* **Tech Stack:** `Python`, `Pandas`, `Power BI`, `DAX`, `Data Wrangling`, `Star Schema`, `UI/UX Design`

### 2. Financial Credit Risk Analytics & Multi-Model Benchmarking
* **Domain:** Corporate Finance & Risk Management (Taiwan Credit Dataset - 30,000 records)
* **Framework:** Supervised Binary Classification (Logistic Regression, Decision Trees, Random Forest)
* **Technical Highlights:** Mitigated extreme class imbalance using automated cost-sensitive learning (`class_weight='balanced'`). Engineered domain-specific metrics (`UTILIZATION_RATE`) to isolate financial exposure thresholds.
* **Business Outcome:** Selected **Random Forest** as the champion model (**0.761 ROC-AUC**), optimizing the precision-recall frontier to capture high-risk defaulters while minimizing false alarms for credit underwriters.
* **Tech Stack:** `Python`, `Scikit-Learn`, `Class Imbalance`, `Feature Engineering`, `ROC-AUC`, `Financial Risk`

### 3. Customer Segmentation via RFM Behavioral Clustering
* **Domain:** E-Commerce & Growth Marketing Operations
* **Framework:** Unsupervised Machine Learning (K-Means Clustering)
* **Technical Highlights:** Implemented feature standardization via `StandardScaler` to remove distance metric bias. Evaluated cluster quality via the **Elbow Method (Inertia)** and **Silhouette Coefficient Analysis** to establish optimal cluster boundaries at $K=3$.
* **Business Outcome:** Segmented customers into three distinct lifecycle cohorts (*Dormant/At-Risk*, *High-Value Loyalists*, and *Recent Core Buyers*) to drive automated re-engagement workflows and loyalty incentives.
* **Tech Stack:** `Python`, `K-Means`, `Unsupervised Learning`, `RFM Modeling`, `Silhouette Analysis`

### 4. Healthcare Churn Predictive Modeling & Patient Retention
* **Domain:** Private Healthcare Insurance & Subscription Retention
* **Framework:** Ensemble Machine Learning (Random Forest Classifier)
* **Technical Highlights:** Handled multi-variable demographic telemetry using stratified partitions. Analyzed continuous Precision-Recall curves and extracted structural **Feature Importance** matrices to determine attrition drivers.
* **Business Outcome:** Isolated operational friction points (`Customer_Service_Calls`) over pricing elasticity as the primary attrition factor, enabling early intervention playbooks before subscription renewal cycles.
* **Tech Stack:** `Python`, `Scikit-Learn`, `Random Forest`, `Precision-Recall`, `Feature Importance`

### 5. Predictive Sales Forecasting & Supply Chain Optimization
* **Domain:** Retail Logistics & Inventory Planning
* **Framework:** Multivariate Linear Regression (Ordinary Least Squares - OLS)
* **Technical Highlights:** Executed multivariate Pearson correlation diagnostics to isolate price elasticity and seasonal trends without multi-collinearity variance.
* **Business Outcome:** Achieved an **$R^2$ score of 0.960** with a **Mean Absolute Error (MAE) of 98.76 units**, establishing an automated stock reordering threshold that minimizes dead inventory overhead.
* **Tech Stack:** `Python`, `Linear Regression`, `Pearson Correlation`, `Demand Forecasting`, `Supply Chain`

### 6. Donor Behavior Analysis & Campaign Impact Assessment
* **Domain:** Non-Profit Fundraising & Campaign Performance
* **Framework:** Time-Series Behavioral Analytics & Interactive Web Application
* **Technical Highlights:** Audited transactional donation logs, corrected temporal anomalies, and deployed a production web app for dynamic segment exploration.
* **Business Outcome:** Delivered an interactive analytics dashboard isolating donor acquisition cohorts and retention shifts following the June 2026 campaign.
* **Tech Stack:** `Python`, `Streamlit Cloud`, `Data Hygiene`, `Cohort Analysis`, `Interactive Viz`
* **Live App:** 👉 **[View Donor Analytics Dashboard on Streamlit Cloud](https://nini-donor-analytics-dashboard.streamlit.app/)**

### 7. SpaceX Falcon 9 First-Stage Landing Prediction
* **Domain:** Aerospace Telemetry & Advanced Predictive Analytics (IBM Capstone)
* **Framework:** Supervised Multi-Model Classification (Logistic Regression, Trees, SVM, KNN)
* **Technical Highlights:** Extracted telemetry data using `BeautifulSoup` and REST APIs. Built interactive geospatial maps (`Folium`) for launch-site spatial analysis and fine-tuned models via `GridSearchCV`.
* **Business Outcome:** Engineered a high-accuracy predictive classification pipeline to determine first-stage rocket recovery feasibility, enabling commercial launch cost benchmarking.
* **Tech Stack:** `Python`, `REST API`, `Web Scraping`, `Folium`, `GridSearchCV`, `Classification`
* **Repository:** 👉 **[View SpaceX Falcon 9 Project Repository](https://github.com/NiNaCocaZero/SpaceX-Falcon9-Predictive-Analysis)**

---

## 🛠️ Technical Stack & Tooling

* **Languages & Core Libraries:** Python (`Pandas`, `NumPy`, `Scikit-Learn`, `SciPy`)
* **Business Intelligence & Visualization:** Power BI, DAX, Star Schema Modeling, Streamlit, Matplotlib, Seaborn, Folium, Plotly
* **Data Engineering & ETL:** Automated Preprocessing Scripts, Feature Engineering, REST APIs, Web Scraping (`BeautifulSoup`)
* **Methodologies:** CRISP-DM, Supervised/Unsupervised Machine Learning, Hypothesis Testing, Time-Series Analysis

---

## 📫 Professional Engagements & Inquiries
Available for contract roles, end-to-end dashboard development, and custom machine learning pipeline engineering.

* **Upwork Profile:** [View Freelance Profile & Hire](https://www.upwork.com/freelancers/ninidata)
* **GitHub Portfolio:** [github.com/NiNaCocaZero](https://github.com/NiNaCocaZero)
