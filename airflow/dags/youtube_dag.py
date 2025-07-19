from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os
import sys

# Add script path to sys.path
sys.path.append("/opt/airflow/scripts")

from extract import fetch_youtube_trending
from transform import transform_data
from load import load_to_postgres  # ✅ updated function

# Constants
default_args = {
    "owner": "vamshi",
    "start_date": datetime(2024, 1, 1),
    "retries": 1
}

with DAG(
    dag_id="youtube_trending_pipeline",
    default_args=default_args,
    schedule=None,  # You can change to "0 8 * * *" for daily 8 AM
    catchup=False,
    description="Extract, transform, and load YouTube trending data to PostgreSQL",
    tags=["youtube", "etl", "postgres"]
) as dag:

    extract_task = PythonOperator(
        task_id="extract_data",
        python_callable=fetch_youtube_trending
    )

    transform_task = PythonOperator(
        task_id="transform_data",
        python_callable=transform_data
    )

    load_task = PythonOperator(
        task_id="load_data_to_postgres",
        python_callable=load_to_postgres  # ✅ new Postgres loader
    )

    extract_task >> transform_task >> load_task
