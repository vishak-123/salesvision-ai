import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.layers import Input

# Load data
df = pd.read_csv("sales.csv")

# Convert date properly
df["date"] = pd.to_datetime(df["date"])

sales = df["sales"].values.reshape(-1, 1)

# Scale data
scaler = MinMaxScaler()
scaled_sales = scaler.fit_transform(sales)

# Create sequences
def create_sequences(data, window=3):
    X, y = [], []
    for i in range(len(data) - window):
        X.append(data[i:i+window])
        y.append(data[i+window])
    return np.array(X), np.array(y)

X, y = create_sequences(scaled_sales)

# Build model
model = Sequential([
    Input(shape=(3, 1)),
    LSTM(50, activation="relu"),
    Dense(1)
])

model.compile(optimizer="adam", loss="mse")
model.fit(X, y, epochs=200, verbose=0)

# Forecast next 30 days
forecast = []
last_sequence = scaled_sales[-3:]

for _ in range(30):
    input_seq = last_sequence.reshape(1, 3, 1)
    pred = model.predict(input_seq, verbose=0)
    forecast.append(pred[0][0])
    last_sequence = np.append(last_sequence[1:], pred, axis=0)

forecast = scaler.inverse_transform(
    np.array(forecast).reshape(-1, 1)
)

# Create future dates
last_date = df["date"].iloc[-1]
future_dates = pd.date_range(
    start=last_date + pd.Timedelta(days=1),
    periods=30,
    freq="D"
)

# Plot
plt.figure(figsize=(10,5))
plt.plot(df["date"], df["sales"], label="Actual Sales")
plt.plot(future_dates, forecast.flatten(), label="Forecast (30 Days)")
plt.legend()
plt.title("30-Day AI Sales Forecast")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.grid(True)
plt.show()
