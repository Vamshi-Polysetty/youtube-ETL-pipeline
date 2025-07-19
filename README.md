# 📊 YouTube Trending ETL Pipeline with Streamlit Dashboard

This project is a complete end-to-end ETL (Extract, Transform, Load) data pipeline that collects trending YouTube video data, processes it using Apache Airflow, stores it in a PostgreSQL database, and visualizes insights using a Streamlit dashboard.

---

## 🚀 Project Overview

- **ETL Workflow**: Managed with Apache Airflow (Dockerized)
- **Data Source**: YouTube Trending Video Data (static or via API)
- **Storage**: PostgreSQL (Dockerized)
- **Visualization**: Streamlit dashboard with data filters and insights

---

## 🧱 Folder Structure

YT_ETL/
├── airflow/
│ ├── dags/
│ │ └── youtube_dag.py
│ ├── scripts/
│ │ ├── extract.py
│ │ ├── transform.py
│ │ └── load.py
│ ├── logs/
│ └── airflow.cfg, airflow.db*, ...
├── docker-compose.yml
├── Dockerfile

output/
├── app.py # Streamlit dashboard
├── check_postgres.py # PostgreSQL connection test


---

## ⚙️ How It Works

1. **Extract**: Raw video data is collected (can be via API or CSV)
2. **Transform**: Cleans and standardizes the data
3. **Load**: Inserts data into a PostgreSQL table `trending_videos`
4. **Visualize**: Streamlit app queries the DB and shows insights

---

## 📦 Setup Instructions

### 1️⃣ Start Airflow & PostgreSQL with Docker

Open terminal and run:

```bash
cd YT_ETL
docker-compose up --build
```
This command builds and starts both the Airflow and PostgreSQL containers.


### 2️⃣ Start Airflow & PostgreSQL Containers

```bash
cd YT_ETL
docker-compose up --build
```

**Airflow UI**: http://localhost:8080 (Default login: airflow / airflow)
**PostgreSQL**: accessible via localhost:5433

### 3️⃣ Trigger the Airflow DAG

Go to http://localhost:8080
Trigger the DAG youtube_dag to start the ETL process

### 4️⃣ Start Streamlit Dashboard
In a new terminal:
```bash
cd output
streamlit run app.py
```
Visit http://localhost:8501 to view your dashboard.

---

### ✅ Features
🌀 Modular DAG for ETL tasks (Extract → Transform → Load)
📈 Clean and interactive Streamlit UI for trend analysis
🐳 Docker-based setup for portability and ease of deployment
🐘 PostgreSQL integration for production-grade structured storage

---