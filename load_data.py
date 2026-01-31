import pandas as pd

# Load sales data
df = pd.read_csv("sales.csv")

print("Sales Data:")
print(df)

print("\nTotal rows:", len(df))
