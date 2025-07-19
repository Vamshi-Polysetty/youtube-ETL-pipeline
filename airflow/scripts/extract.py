# extract.py

import os
import requests
import json

DATA_DIR = "/opt/airflow/data" 


API_KEY = "YOUR_SECRET_API-KEY" # place your secret api key here
REGION = "IN"
URL = f"https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics&chart=mostPopular&regionCode={REGION}&maxResults=50&key={API_KEY}"

def fetch_youtube_trending():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        with open(os.path.join(DATA_DIR, "raw_data.json"), "w") as f:
            json.dump(data, f, indent=2)
        print("✅ Data extracted and saved.")
    else:
        print("❌ Failed to fetch data:", response.status_code)

if __name__ == "__main__":
    fetch_youtube_trending()
