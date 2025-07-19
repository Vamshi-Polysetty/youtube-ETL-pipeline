import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text

# PostgreSQL connection setup
engine = create_engine("postgresql+psycopg2://vamshi:secret@localhost:5433/yt_trending")

# Streamlit page settings
st.set_page_config(page_title="YouTube Trending Dashboard", layout="wide")
st.title("📺 YouTube Trending Dashboard")

# Load data from DB
@st.cache_data
def load_data():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM trending_videos"))
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
    return df

df = load_data()

# Optional filters
with st.sidebar:
    st.header("🔍 Filters")
    selected_channels = st.multiselect("Filter by Channel:", options=df["channel"].unique())
    df["published_date"] = pd.to_datetime(df["published_at"]).dt.date
    selected_date = st.date_input("Filter by Publish Date:", value=None)

# Apply filters
if selected_channels:
    df = df[df["channel"].isin(selected_channels)]
if selected_date:
    df = df[df["published_date"] == selected_date]

# Show results as card-style video entries
st.subheader("🔥 Trending Videos")

for index, row in df.iterrows():
    video_url = f"https://www.youtube.com/watch?v={row['video_id']}"
    thumbnail_url = f"https://img.youtube.com/vi/{row['video_id']}/0.jpg"
    
    st.markdown("---")
    cols = st.columns([1, 4])

    # Thumbnail (Left)
    with cols[0]:
        st.image(thumbnail_url, width=180)

    # Info (Right)
    with cols[1]:
        st.markdown(f"### [{row['title']}]({video_url})", unsafe_allow_html=True)
        st.markdown(f"**Channel:** {row['channel']}")
        st.markdown(
            f"👁️ **Views:** {row['views']} &nbsp;&nbsp; 👍 **Likes:** {row['likes']} &nbsp;&nbsp; 💬 **Comments:** {row['comments']}"
        )
        st.markdown(f"🗓️ **Published:** {row['published_at']}")
