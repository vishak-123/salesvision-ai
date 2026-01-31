import pandas as pd
import numpy as np
import joblib
from tensorflow.keras.models import load_model

# Load model and scaler
model = load_model("sales_forecast_model.keras")
scaler = joblib.load("scaler.save")

# Load data
df = pd.read_csv("sales.csv")

sales = df["sales"].values.reshape(-1, 1)
scaled_sales = scaler.transform(sales)

# Forecast
window = 3
last_seq = scaled_sales[-window:]

forecast = []

for _ in range(30):
    pred = model.predict(last_seq.reshape(1, window, 1), verbose=0)
    forecast.append(pred[0][0])
    last_seq = np.append(last_seq[1:], pred, axis=0)

forecast = scaler.inverse_transform(
    np.array(forecast).reshape(-1, 1)
)

print("\n📈 NEXT 30 DAYS SALES FORECAST:\n")
print(forecast.flatten())
