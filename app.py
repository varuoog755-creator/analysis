import streamlit as st
import pandas as pd
from trend_engine import TrendEngine
import plotly.express as px
from viral_card import ViralCardGenerator
import os
import json
import time

# Page Config
st.set_page_config(page_title="TrendPulse | AI Market Intelligence", page_icon="📈", layout="wide")

# Load Fleet Results
def load_fleet_data():
    path = os.path.join(os.path.dirname(__file__), "agent_results.json")
    if os.path.exists(path):
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except:
            pass
    return {"findings": [], "last_run": None, "active_agents": []}

# Custom CSS for Premium Look
st.markdown("""
    <style>
    .main { background: #0F172A !important; color: white !important; }
    .stApp { background: #0F172A; }
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] { height: 50px; white-space: pre-wrap; background-color: #1E293B; border-radius: 10px 10px 0px 0px; color: white; padding-left: 20px; padding-right: 20px; }
    .stTabs [aria-selected="true"] { background-color: #4F46E5 !important; }
    .agent-tag { background: #4F46E5; color: white; padding: 2px 8px; border-radius: 5px; font-size: 0.8em; font-weight: bold; }
    .finding-card { background: #1E293B; padding: 20px; border-radius: 15px; border-left: 5px solid #06B6D4; margin-bottom: 15px; }
    </style>
    """, unsafe_allow_html=True)

st.title("📈 TrendPulse")
st.caption("Autonomous Niche Market Intelligence Fleet")

# Sidebar
st.sidebar.title("🛠️ Control Center")
use_demo = st.sidebar.checkbox("Demo Mode", value=False)
if st.sidebar.button("🧹 Clear Cache"):
    st.sidebar.success("Cache cleared!")

st.sidebar.divider()
st.sidebar.write("### 💎 SaaS Status")
if st.sidebar.button("🚀 Upgrade to Founder ($49/mo)"):
    st.sidebar.balloons()
    st.sidebar.info("Validation Signal Captured! 📈 (Step 4)")

# Tabs
tab_search, tab_fleet, tab_public = st.tabs(["🔍 Manual Search", "🤖 Autonomous Fleet (24/7)", "🌐 Public Market Report"])

engine = TrendEngine()

with tab_search:
    st.write("### Deep Niche Analysis")
    keyword = st.text_input("Enter a keyword to analyze:", placeholder="e.g. AI Coding Agents, Vegan Pet Food")
    
    if keyword:
        with st.spinner(f"Agents are scanning for '{keyword}'..."):
            col1, col2 = st.columns(2)
            
            # Google Trends
            with col1:
                st.subheader("Google Search Interest")
                if use_demo:
                    dates = pd.date_range(start='1/1/2024', periods=52, freq='W')
                    import numpy as np
                    gt_data = pd.DataFrame({keyword: np.random.randint(20, 100, size=52)}, index=dates)
                    st.info("⚠️ Demo Mode Active")
                else:
                    gt_data = engine.get_google_trends(keyword)
                
                if not gt_data.empty:
                    fig_gt = px.line(gt_data, y=keyword, title="Interest Over Time")
                    fig_gt.update_traces(line_color='#FF4B4B', line_width=3)
                    st.plotly_chart(fig_gt, use_container_width=True)
                else:
                    st.warning("No Google data found.")

            # Hacker News
            with col2:
                st.subheader("Hacker News Mentions")
                if use_demo:
                    hn_data = pd.DataFrame({'hn_mentions': [10, 25, 15, 40]}, index=pd.date_range(start='1/1/2024', periods=4))
                else:
                    hn_data = engine.get_hacker_news_mentions(keyword)
                
                if not hn_data.empty:
                    fig_hn = px.bar(hn_data, y='hn_mentions', title="Story Mentions")
                    fig_hn.update_traces(marker_color='#FF914D')
                    st.plotly_chart(fig_hn, use_container_width=True)
                else:
                    st.warning("No HN mentions found.")

            # X.com
            st.divider()
            st.subheader("🐦 X.com (Twitter) Pulse")
            x_data = engine.get_x_trends(keyword) if not use_demo else pd.DataFrame([{"text": "Trending high!", "likes": 500, "user": "AlphaHunter"}])
            
            if not x_data.empty:
                for _, row in x_data.iterrows():
                    st.markdown(f"**@{row.get('user', 'User')}**: {row['text']}")
                    st.caption(f"❤️ {row.get('likes', 0)}")
            else:
                st.warning("No real-time tweets found.")

            # Viral Card
            if not gt_data.empty:
                st.divider()
                if st.button("🚀 Generate Viral Share Card"):
                    with st.spinner("Designing your report..."):
                        gen = ViralCardGenerator()
                        path = gen.generate_viral_card(keyword, gt_data)
                        st.image(path)
                        st.success(f"Report ready: {path}")

            # RSS Intelligence (Phase 2)
            st.divider()
            st.subheader("📡 RSS Intelligence (Phase 2)")
            rss_data = engine.get_rss_trends(keyword)
            if not rss_data.empty:
                for _, entry in rss_data.iterrows():
                    with st.container():
                        st.markdown(f"**[{entry['title']}]({entry['link']})**")
                        st.caption(f"Source: {entry['source']} | Published: {entry['published']}")
            else:
                st.info("No RSS feeds found for this niche.")

with tab_fleet:
    fleet_data = load_fleet_data()
    
    # Header Stats
    s1, s2, s3 = st.columns(3)
    with s1:
        st.metric("Agents Active", "3")
        st.caption("Researcher, Designer, Janitor")
    with s2:
        status = "🟢 ON PULSE" if fleet_data.get("active_agents") else "⚪ SLEEPING"
        st.metric("Fleet Status", status)
    with s3:
        st.metric("Total Insights", len(fleet_data.get("findings", [])))

    st.divider()
    
    if fleet_data["findings"]:
        st.write("### 📡 Autonomous Findings Feed")
        for finding in fleet_data["findings"]:
            st.markdown(f"""
            <div class="finding-card">
                <h4>{finding['keyword']} <span class="agent-tag">{finding['source']}</span></h4>
                <p>Strength Score: {'🔥' * (finding['strength'] // 2 + 1)}</p>
                <p style="font-size: 0.8em; color: #94A3B8;">Detected: {finding['timestamp']}</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("The Fleet is currently deployed. New results appear every 4 hours.")
        if st.button("⚡ Force Agent Pulse"):
            os.system("python fleet_engine.py")
            st.rerun()

with tab_public:
    st.write("### 🌐 Live Public Intelligence")
    st.info("This section is visible to all TrendPulse clients to maintain market transparency.")
    
    # Show the latest 5 autonomous findings in a premium table
    if fleet_data["findings"]:
        df_public = pd.DataFrame(fleet_data["findings"])
        # Format for table
        st.dataframe(
            df_public[['keyword', 'strength', 'timestamp', 'source']].tail(10),
            use_container_width=True,
            hide_index=True
        )
        
        st.divider()
        st.write("### 💎 Want Full Access?")
        st.button("Contact Support for API Access", key="public_api_btn")
    else:
        st.warning("No public data available yet. Please allow the agents to complete their first pulse.")
