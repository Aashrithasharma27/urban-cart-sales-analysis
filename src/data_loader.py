import pandas as pd

# Load the dataset
df = pd.read_csv("data/raw/urban_cart_sales.csv")

print("Urban Cart Sales Dataset Loaded Successfully!\n")

# First 5 rows
print("First 5 Rows:")
print(df.head())

# Last 5 rows
print("\nLast 5 Rows:")
print(df.tail())

# Shape
print("\nDataset Shape:")
print(df.shape)

# Columns
print("\nColumn Names:")
print(df.columns.tolist())

# Dataset information
print("\nDataset Information:")
df.info()

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())