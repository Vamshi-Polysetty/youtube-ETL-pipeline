# transform.py

import json
import os
import pandas as pd

DATA_DIR = "/opt/airflow/data" 

def transform_data():
    with open(os.path.join(DATA_DIR, "raw_data.json"), "r") as f:
        data = json.load(f)

    videos = data["items"]
    records = []
    for video in videos:
        snippet = video["snippet"]
        stats = video["statistics"]
        records.append({
            "video_id": video["id"],
            "title": snippet["title"],
            "published_at": snippet["publishedAt"],
            "channel": snippet["channelTitle"],
            "views": stats.get("viewCount", 0),
            "likes": stats.get("likeCount", 0),
            "comments": stats.get("commentCount", 0)
        })

    df = pd.DataFrame(records)
    df.to_csv(os.path.join(DATA_DIR, "clean_data.csv"), index=False)
    print("✅ Data transformed and saved. clean_data.csv")

if __name__ == "__main__":
    transform_data()
