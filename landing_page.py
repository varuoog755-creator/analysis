import streamlit as st
import os

# Page Config
st.set_page_config(page_title="TrendPulse | Stop Guessing, Start Dominating", page_icon="🚀", layout="wide")

# Custom CSS for Premium Landing Page
st.markdown("""
    <style>
    .main { background: #020617 !important; color: white !important; }
    .stApp { background: #020617; }
    
    .hero-title { font-size: 4rem; font-weight: 800; background: linear-gradient(90deg, #4F46E5, #06B6D4); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 0px; }
    .hero-subtitle { font-size: 1.5rem; color: #94A3B8; margin-bottom: 2rem; }
    
    .feature-card { background: rgba(30, 41, 59, 0.5); padding: 30px; border-radius: 20px; border: 1px solid rgba(255, 255, 255, 0.1); text-align: center; height: 100%; transition: 0.3s; }
    .feature-card:hover { transform: translateY(-10px); border-color: #4F46E5; box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.2); }
    
    .pricing-card { background: #1E293B; padding: 40px; border-radius: 24px; border: 1px solid #334155; text-align: center; }
    .pricing-card.popular { border: 2px solid #4F46E5; position: relative; }
    .popular-tag { position: absolute; top: -15px; left: 50%; transform: translateX(-50%); background: #4F46E5; color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.8rem; font-weight: bold; }
    
    .cta-button { background: linear-gradient(90deg, #4F46E5, #06B6D4) !important; color: white !important; padding: 15px 40px !important; border-radius: 12px !important; font-size: 1.2rem !important; font-weight: bold !important; border: none !important; cursor: pointer; }
    </style>
    """, unsafe_allow_html=True)

# Navigation
cols = st.columns([1, 4, 1])
with cols[0]: st.subheader("📈 TrendPulse")
with cols[2]: 
    if st.button("Login"): st.success("Demo Mode Access")

# Hero Section
st.markdown("<br><br>", unsafe_allow_html=True)
c1, c2, c3 = st.columns([1, 8, 1])
with c2:
    st.markdown("<h1 class='hero-title' style='text-align: center;'>Autonomously Discover Your Next $10k/mo Niche</h1>", unsafe_allow_html=True)
    st.markdown("<p class='hero-subtitle' style='text-align: center;'>TrendPulse uses an autonomous fleet of AI agents to scan X.com, Hacker News, and Google Trends 24/7. We find the signals while your competitors are still sleeping.</p>", unsafe_allow_html=True)
    
    st.markdown("<div style='text-align: center;'><button class='cta-button'>Start Free Trial (No CC Required)</button></div>", unsafe_allow_html=True)

st.markdown("<br><br><br>", unsafe_allow_html=True)

# Features Section
st.write("### 🛠️ Built for the 2026 SaaS Economy")
f1, f2, f3 = st.columns(3)
with f1:
    st.markdown("""
    <div class='feature-card'>
        <h3>🤖 Autonomous Fleet</h3>
        <p>3 specialized agents (Researcher, Content, Janitor) work 24/7 on your VPS to verify data moats.</p>
    </div>
    """, unsafe_allow_html=True)
with f2:
    st.markdown("""
    <div class='feature-card'>
        <h3>🐦 Real-Time X Pulse</h3>
        <p>Deep sentiment analysis on X.com (Twitter) to find "What people are complaining about" daily.</p>
    </div>
    """, unsafe_allow_html=True)
with f3:
    st.markdown("""
    <div class='feature-card'>
        <h3>📱 OpenClaw Bridge</h3>
        <p>Control your intelligence fleet via WhatsApp. Ask "What should I build today?" while on the go.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br><br>", unsafe_allow_html=True)

# Pricing Section (Step 6)
st.write("### 💎 Simple, Scalable Pricing")
p1, p2, p3 = st.columns(3)

with p1:
    st.markdown("""
    <div class='pricing-card'>
        <h3>Hacker</h3>
        <h2 style='margin: 0;'>$0 <span style='font-size: 1rem; color: #94A3B8;'>/mo</span></h2>
        <ul style='text-align: left; list-style: none; padding: 20px 0;'>
            <li>✅ 3 Manual Searches / day</li>
            <li>✅ Basic Google Trends</li>
            <li>❌ 24/7 Background Fleet</li>
        </ul>
        <button style='width: 100%; padding: 10px; border-radius: 8px; border: 1px solid #4F46E5; background: none; color: white;'>Get Started</button>
    </div>
    """, unsafe_allow_html=True)

with p2:
    st.markdown("""
    <div class='pricing-card popular'>
        <div class='popular-tag'>MOST POPULAR</div>
        <h3>Founder</h3>
        <h2 style='margin: 0;'>$49 <span style='font-size: 1rem; color: #94A3B8;'>/mo</span></h2>
        <ul style='text-align: left; list-style: none; padding: 20px 0;'>
            <li>✅ Unlimited Searches</li>
            <li>✅ Viral Card Downloads</li>
            <li>✅ 1x Autonomous Agent</li>
            <li>✅ Priority X.com Data</li>
        </ul>
        <button class='cta-button' style='width: 100%; font-size: 1rem !important;'>Claim This Offer</button>
    </div>
    """, unsafe_allow_html=True)

with p3:
    st.markdown("""
    <div class='pricing-card'>
        <h3>Enterprise</h3>
        <h2 style='margin: 0;'>$199 <span style='font-size: 1rem; color: #94A3B8;'>/mo</span></h2>
        <ul style='text-align: left; list-style: none; padding: 20px 0;'>
            <li>✅ Full Multi-Agent Fleet</li>
            <li>✅ OpenClaw (WhatsApp) Integration</li>
            <li>✅ White-label Reports</li>
            <li>✅ API Access</li>
        </ul>
        <button style='width: 100%; padding: 10px; border-radius: 8px; border: 1px solid #4F46E5; background: none; color: white;'>Contact Sales</button>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #475569;'>© 2026 TrendPulse AI. All rights reserved.</p>", unsafe_allow_html=True)
