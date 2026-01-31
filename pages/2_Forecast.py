# ===============================
# Forecast Center — SalesVision AI
# ===============================

from auth import require_role
require_role(["admin", "user"])

import streamlit as st
import pandas as pd
import numpy as np
import time
import joblib
import plotly.graph_objects as go
from tensorflow.keras.models import load_model

from ui import load_ui

# -------------------------------
# Load UI
# -------------------------------
load_ui()

# -------------------------------
# Page Title
# -------------------------------
st.markdown("<h1>📈 Forecast Center</h1>", unsafe_allow_html=True)
st.caption("AI-powered time series sales forecasting using LSTM")

st.markdown("---")

# -------------------------------
# Load dataset
# -------------------------------
df = pd.read_csv("sales.csv")
df["date"] = pd.to_datetime(df["date"])

# -------------------------------
# Load model & scaler
# -------------------------------
model = load_model("sales_forecast_model.keras", compile=False)
scaler = joblib.load("scaler.save")

# -------------------------------
# Forecast settings
# -------------------------------
days = st.slider(
    "📅 Select forecast days",
    min_value=7,
    max_value=180,
    value=30
)

# -------------------------------
# Forecast button
# -------------------------------
if st.button("🚀 Run AI Forecast"):

    with st.spinner("🤖 AI is analyzing sales patterns and generating predictions..."):
        time.sleep(2)

        sales = df["sales"].values.reshape(-1, 1)
        scaled = scaler.transform(sales)

        last = scaled[-3:]
        forecast = []

        for _ in range(days):
            pred = model.predict(last.reshape(1, 3, 1), verbose=0)
            forecast.append(pred[0][0])
            last = np.append(last[1:], pred, axis=0)

        forecast = scaler.inverse_transform(
            np.array(forecast).reshape(-1, 1)
        )

        future_dates = pd.date_range(
            df["date"].iloc[-1] + pd.Timedelta(days=1),
            periods=days
        )

    st.success("✅ Forecast completed successfully")

    # -------------------------------
    # Plot result
    # -------------------------------
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df["date"],
            y=df["sales"],
            name="Actual Sales",
            line=dict(color="#22c55e")
        )
    )

    fig.add_trace(
        go.Scatter(
            x=future_dates,
            y=forecast.flatten(),
            name="AI Forecast",
            line=dict(color="#6366f1", dash="dash")
        )
    )

    fig.update_layout(
        template="plotly_dark",
        height=500,
        margin=dict(l=20, r=20, t=40, b=20),
        legend=dict(orientation="h"),
        title="Sales Forecast Visualization"
    )

    st.plotly_chart(fig, use_container_width=True)

else:
    st.info("⬆️ Click **Run AI Forecast** to generate predictions")
