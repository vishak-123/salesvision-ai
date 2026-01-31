from login import login_page
import streamlit as st
from ui import load_ui

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="SalesVision AI",
    layout="wide"
)

# ================= LOAD UI THEME =================
load_ui()
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login_page()
    st.stop()


# ================= SIDEBAR =================
with st.sidebar:

    if st.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.rerun()


    st.image(
        "https://cdn-icons-png.flaticon.com/512/4712/4712109.png",
        width=70
    )

    st.markdown("## 🚀 SalesVision AI")
    st.caption("Enterprise Forecasting Platform")

    st.markdown("""
    🔹 AI Sales Forecasting  
    🔹 Deep Learning (LSTM)  
    🔹 Business Intelligence  
    🔹 Global Ready Platform  
    """)


# ================= HERO SECTION =================
st.markdown("""
<div class="hero">
    <h1>SalesVision AI</h1>
    <p>Intelligent Sales Forecasting & Business Intelligence Platform</p>
</div>
""", unsafe_allow_html=True)

# ================= FEATURE CARDS =================
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="glass-card">
        <img src="https://cdn-icons-png.flaticon.com/512/2103/2103633.png" width="55">
        <h3>AI Forecasting</h3>
        <p>Predict future sales using deep learning time-series models.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="glass-card">
        <img src="https://cdn-icons-png.flaticon.com/512/2920/2920244.png" width="55">
        <h3>Smart Insights</h3>
        <p>Automatic AI-generated business insights and growth analysis.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="glass-card">
        <img src="https://cdn-icons-png.flaticon.com/512/4321/4321241.png" width="55">
        <h3>Advanced Analytics</h3>
        <p>Interactive KPIs and visual business intelligence dashboards.</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="glass-card">
        <img src="https://cdn-icons-png.flaticon.com/512/854/854878.png" width="55">
        <h3>Global Ready</h3>
        <p>Upload any dataset and forecast instantly worldwide.</p>
    </div>
    """, unsafe_allow_html=True)

# ================= FOOTER =================
st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<center style="color:#94a3b8;">
    <h4>AI Project — Built by Vishak Kuppusamy</h4>
</center>
""", unsafe_allow_html=True)
