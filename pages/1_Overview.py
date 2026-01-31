import streamlit as st
import pandas as pd
import time
from ui import load_ui
from auth import require_role

require_role(["admin"])
load_ui()


st.markdown("<h1>📊 Executive Overview</h1>", unsafe_allow_html=True)

df = pd.read_csv("sales.csv")

total = int(df["sales"].sum())
avg = int(df["sales"].mean())
maxv = int(df["sales"].max())
minv = int(df["sales"].min())

c1, c2, c3, c4 = st.columns(4)

with c1:
    with st.spinner("Loading KPI..."):
        time.sleep(0.4)
    st.metric("💰 Total Sales", total)

with c2:
    with st.spinner("Calculating..."):
        time.sleep(0.4)
    st.metric("📊 Average Sales", avg)

with c3:
    with st.spinner("Analyzing..."):
        time.sleep(0.4)
    st.metric("📈 Highest Sale", maxv)

with c4:
    with st.spinner("Processing..."):
        time.sleep(0.4)
    st.metric("📉 Lowest Sale", minv)

st.markdown("---")
st.subheader("📄 Sales Dataset")
st.markdown("""
<hr style="border:1px solid #334155; margin-top:30px; margin-bottom:20px;">
<h3>📊 Detailed Sales Table</h3>
""", unsafe_allow_html=True)

st.dataframe(df, use_container_width=True)

