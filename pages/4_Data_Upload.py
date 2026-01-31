from auth import require_role
require_role(["admin"])
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import joblib
from tensorflow.keras.models import load_model

st.title("📥 Upload Your Sales Data")

st.info("Upload CSV file with columns: **date, sales**")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    if "date" not in df.columns or "sales" not in df.columns:
        st.error("CSV must contain 'date' and 'sales' columns")
    else:
        df["date"] = pd.to_datetime(df["date"])
        st.success("✅ File uploaded successfully")

        st.dataframe(df.head())

        # Load model
        model = load_model("sales_forecast_model.keras")
        scaler = joblib.load("scaler.save")

        sales = df["sales"].values.reshape(-1, 1)
        scaled_sales = scaler.transform(sales)

        days = st.slider("Forecast days", 7, 90, 30)

        window = 3
        last_seq = scaled_sales[-window:]

        forecast = []

        for _ in range(days):
            pred = model.predict(last_seq.reshape(1, window, 1), verbose=0)
            forecast.append(pred[0][0])
            last_seq = np.append(last_seq[1:], pred, axis=0)

        forecast = scaler.inverse_transform(
            np.array(forecast).reshape(-1, 1)
        )

        future_dates = pd.date_range(
            df["date"].iloc[-1] + pd.Timedelta(days=1),
            periods=days
        )

        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=df["date"],
            y=df["sales"],
            name="Actual",
            mode="lines+markers"
        ))

        fig.add_trace(go.Scatter(
            x=future_dates,
            y=forecast.flatten(),
            name="Forecast",
            mode="lines+markers"
        ))

        fig.update_layout(
            title="Forecast from Uploaded Data",
            template="plotly_dark",
            height=550
        )

        st.plotly_chart(fig, use_container_width=True)
