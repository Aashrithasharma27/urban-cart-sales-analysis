import pandas as pd
from pathlib import Path

# Project root folder
project_root = Path(__file__).resolve().parent.parent

# File paths
input_file = project_root / "data" / "raw" / "urban_cart_sales.csv"
output_file = project_root / "data" / "processed" / "cleaned_sales.csv"

# Read dataset
df = pd.read_csv(input_file)

print("Original Dataset Shape:", df.shape)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Convert Order_Date into datetime format
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Check data types
print("\nData Types:")
print(df.dtypes)

# Save cleaned dataset
df.to_csv(output_file, index=False)

print("\nCleaned dataset saved successfully!")
print(f"Location: {output_file}")