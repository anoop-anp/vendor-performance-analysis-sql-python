# 📊 Vendor Performance Analysis

\### SQL + Python End-to-End Data Pipeline Project



This project analyzes vendor performance in a retail inventory system using  

SQL (SQLite) and Python to generate actionable business insights.



The objective is to measure vendor contribution, evaluate profitability,  

and assess inventory efficiency using structured KPI engineering.



---



## 🚀 Project Objective



This project focuses on solving the following business challenges:



\- Identify underperforming brands  

\- Determine top vendors contributing to sales and gross profit  

\- Measure vendor-level profitability  

\- Assess inventory turnover efficiency  



---



## 🏗️ Project Architecture



Raw CSV Files  

⬇  

Chunk-based Data Ingestion (SQLAlchemy)  

⬇  

SQLite Database  

⬇  

SQL CTE Aggregation Queries  

⬇  

Python Data Cleaning \& KPI Engineering  

⬇  

Vendor Summary Table  

⬇  

Exploratory Data Analysis  



---



## 📂 Project Structure



vendor-performance-analysis/



├── README.md

├── requirements.txt

├── .gitignore

│

├── data/

│   ├── begin\_inventory.csv

│   ├── end\_inventory.csv

│   ├── purchase\_prices.csv

│   ├── purchases.csv

│   ├── sales.csv

│   └── vendor\_invoice.csv

│

├── scripts/

│   ├── ingestion\_db.py

│   └── get\_vendor\_summary.py

│

├── notebooks/

│   ├── ExploratoryDataAnalysis.ipynb

│   └── VendorPerformanceAnalysis.ipynb

│

└── database/

---



## ⚙️ Tech Stack



\- SQL (SQLite)

\- Python

\- Pandas

\- NumPy

\- SQLAlchemy

\- Matplotlib

\- Seaborn

\- Jupyter Notebook

\- Logging Module



---



## 🔄 Data Pipeline Flow



### 1️⃣ Data Ingestion (ingestion\_db.py)



\- Reads CSV files in chunks  

\- Creates database tables automatically  

\- Uses SQLAlchemy engine  

\- Logs ingestion progress  



---



### 2️⃣ Vendor Summary Creation (get\_vendor\_summary.py)



Uses SQL CTE queries to:



\- Aggregate purchase data  

\- Aggregate sales data  

\- Combine freight cost  

\- Generate vendor-level summary  



---



## 🧹 Data Cleaning



\- Converted numeric columns to proper data types  

\- Filled missing values  

\- Removed formatting inconsistencies  



---



## 📊 KPIs Generated



\- TotalPurchaseDollars  

\- TotalSalesDollars  

\- GrossProfit  

\- ProfitMargin (%)  

\- StockTurnover  

\- SalesToPurchaseRatio  

\- FreightCost  

\- TotalSalesQuantity  

\- TotalPurchaseQuantity  



---



## 📈 Business Insights Derived



✔ Top vendors by purchase contribution  

✔ Vendor profitability analysis  

✔ Inventory turnover efficiency  

✔ Brand-level performance comparison  



---



## 🧮 Key KPI Formulas



Gross Profit = Total Sales – Total Purchase  



Profit Margin (%) = (Gross Profit / Total Sales) × 100  



Stock Turnover = Sales Quantity / Purchase Quantity  



Sales to Purchase Ratio = Sales Dollars / Purchase Dollars  



---



## ▶️ How To Run This Project



\### Step 1: Clone Repository

git clone <your-repo-link>

\### Step 2: Install Requirements

pip install -r requirements.txt

\### Step 3: Run Data Ingestion

python scripts/ingestion\_db.py

\### Step 4: Generate Vendor Summary

python scripts/get\_vendor\_summary.py

\### Step 5: Run Analysis

Open Jupyter Notebook and execute:

\- ExploratoryDataAnalysis.ipynb

\- VendorPerformanceAnalysis.ipynb



---



## 👨‍💻 Author



Anoop Singh  

📧 Email: anooprjy@gmail.com

