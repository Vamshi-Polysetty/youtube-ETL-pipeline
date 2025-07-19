import pandas as pd
from sqlalchemy import create_engine
import os

DATA_DIR = "/opt/airflow/data"

def load_to_postgres():
    df = pd.read_csv(os.path.join(DATA_DIR, "clean_data.csv"))

    # PostgreSQL connection details
    db_user = "vamshi"
    db_password = "secret"
    db_host = "postgres"
    db_port = "5432"
    db_name = "yt_trending"

    # Create SQLAlchemy engine
    engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

    # Load data into PostgreSQL
    df.to_sql("trending_videos", engine, if_exists="replace", index=False)

    print("✅ Data loaded into PostgreSQL successfully.")

if __name__ == "__main__":
    load_to_postgres()
