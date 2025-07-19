from sqlalchemy import create_engine, text
import pandas as pd

# Create SQLAlchemy engine with explicit psycopg2
engine = create_engine("postgresql+psycopg2://vamshi:secret@localhost:5433/yt_trending")

# Open a real connection
with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM trending_videos LIMIT 5"))
    df = pd.DataFrame(result.fetchall(), columns=result.keys())

print(df)
