import streamlit as st

def load_ui():

    st.markdown("""
    <style>

    /* ===== GLOBAL DARK SAAS THEME ===== */

    .main {
        background: linear-gradient(135deg, #020617, #0f172a);
        color: #e5e7eb;
    }

    h1, h2, h3, h4, p {
        color: #e5e7eb;
    }

    /* Glass cards */
    .glass-card {
        background: rgba(255,255,255,0.08);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border-radius: 22px;
        padding: 28px;
        box-shadow: 0 25px 60px rgba(0,0,0,0.5);
        margin-bottom: 20px;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #020617, #0f172a);
        border-right: 1px solid rgba(255,255,255,0.1);
    }

    section[data-testid="stSidebar"] * {
        color: #e5e7eb !important;
    }

    </style>
    """, unsafe_allow_html=True)
