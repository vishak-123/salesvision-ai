import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Load data
df = pd.read_csv("sales.csv")

# Use only sales column
sales = df["sales"].values.reshape(-1, 1)

# Normalize data (0–1)
scaler = MinMaxScaler()
scaled_sales = scaler.fit_transform(sales)

# Create sequences
def create_sequences(data, window_size=3):
    X = []
    y = []
    for i in range(len(data) - window_size):
        X.append(data[i:i+window_size])
        y.append(data[i+window_size])
    return np.array(X), np.array(y)

X, y = create_sequences(scaled_sales)

print("Input shape:", X.shape)
print("Output shape:", y.shape)
