import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Input
import joblib

# Load data
df = pd.read_csv("sales.csv")
df["date"] = pd.to_datetime(df["date"])

sales = df["sales"].values.reshape(-1, 1)

# Scale
scaler = MinMaxScaler()
scaled_sales = scaler.fit_transform(sales)

# Save scaler
joblib.dump(scaler, "scaler.save")

# Create sequences
def create_sequences(data, window=3):
    X, y = [], []
    for i in range(len(data) - window):
        X.append(data[i:i+window])
        y.append(data[i+window])
    return np.array(X), np.array(y)

X, y = create_sequences(scaled_sales)

# Model
model = Sequential([
    Input(shape=(3, 1)),
    LSTM(50),
    Dense(1)
])

# IMPORTANT: compile with explicit loss object
from tensorflow.keras.losses import MeanSquaredError

model.compile(
    optimizer="adam",
    loss=MeanSquaredError()
)

model.fit(X, y, epochs=200, verbose=1)

# SAVE USING NEW FORMAT
model.save("sales_forecast_model.keras")

print("✅ Model saved in new Keras format")
