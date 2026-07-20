import pandas as pd
from pathlib import Path

# Project root
project_root = Path(__file__).resolve().parent.parent

# Read cleaned dataset
df = pd.read_csv(project_root / "data" / "processed" / "cleaned_sales.csv")

print("=" * 50)
print("URBAN CART SALES ANALYSIS")
print("=" * 50)

# Total Sales
print("\nTotal Sales:")
print(f"₹ {df['Sales'].sum():,.2f}")

# Total Profit
print("\nTotal Profit:")
print(f"₹ {df['Profit'].sum():,.2f}")

# Total Orders
print("\nTotal Orders:")
print(df["Order_ID"].nunique())

# Average Sales
print("\nAverage Sales Per Order:")
print(f"₹ {df['Sales'].mean():,.2f}")

# Top Categories
print("\nSales by Category:")
print(df.groupby("Category")["Sales"].sum().sort_values(ascending=False))

# Top Cities
print("\nTop 10 Cities by Sales:")
print(df.groupby("City")["Sales"].sum().sort_values(ascending=False).head(10))

# Payment Methods
print("\nPayment Method Usage:")
print(df["Payment_Method"].value_counts())

# Shipping Mode
print("\nShipping Mode Usage:")
print(df["Shipping_Mode"].value_counts())

# Top Products
print("\nTop 10 Products by Sales:")
print(df.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(10))