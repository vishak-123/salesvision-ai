from auth import require_role
require_role(["admin", "user"])
import streamlit as st
import pandas as pd
import numpy as np
import joblib
from tensorflow.keras.models import load_model

st.title("🧠 AI Business Insights")

# Load data
df = pd.read_csv("sales.csv")
df["date"] = pd.to_datetime(df["date"])

sales = df["sales"].values.reshape(-1, 1)

# Load model & scaler
model = load_model("sales_forecast_model.keras")
scaler = joblib.load("scaler.save")

# Forecast horizon
days = st.slider("Select Insight Period (days)", 7, 120, 30)

# Scale
scaled_sales = scaler.transform(sales)
window = 3
last_seq = scaled_sales[-window:]

forecast = []

for _ in range(days):
    pred = model.predict(last_seq.reshape(1, window, 1), verbose=0)
    forecast.append(pred[0][0])
    last_seq = np.append(last_seq[1:], pred, axis=0)

forecast = scaler.inverse_transform(
    np.array(forecast).reshape(-1, 1)
).flatten()

# Calculate insights
start_value = forecast[0]
end_value = forecast[-1]
growth_pct = round((end_value - start_value) / start_value * 100, 2)

trend = "Upward 📈" if growth_pct > 0 else "Downward 📉"

# Display insights
st.subheader("📊 AI Generated Insights")

st.success(f"📈 Forecast Trend: **{trend}**")
st.info(f"🔮 Expected Growth: **{growth_pct}%** over next {days} days")

if growth_pct < 0:
    st.error("⚠️ Risk detected: Sales decline expected. Consider promotions.")
elif growth_pct < 5:
    st.warning("⚠️ Low growth detected. Business optimization recommended.")
else:
    st.success("🚀 Strong growth expected. Scale operations confidently.")

st.markdown("---")

st.subheader("🧠 Business Recommendation")

if growth_pct > 10:
    st.write("✅ Increase inventory and marketing spend.")
elif growth_pct > 0:
    st.write("⚖️ Maintain stable strategy and monitor performance.")
else:
    st.write("🔻 Reduce costs and introduce offers to boost demand.")
