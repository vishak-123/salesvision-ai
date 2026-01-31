import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Load data
df = pd.read_csv("sales.csv")
sales = df["sales"].values.reshape(-1, 1)

# Scale
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

# Build LSTM model
model = Sequential()
model.add(LSTM(50, activation="relu", input_shape=(X.shape[1], 1)))
model.add(Dense(1))

model.compile(
    optimizer="adam",
    loss="mse"
)

# Train model
model.fit(X, y, epochs=200, verbose=1)

# Predict next day
last_sequence = scaled_sales[-3:]
last_sequence = last_sequence.reshape(1, 3, 1)

prediction = model.predict(last_sequence)
predicted_sales = scaler.inverse_transform(prediction)

print("Predicted next day sales:", int(predicted_sales[0][0]))
