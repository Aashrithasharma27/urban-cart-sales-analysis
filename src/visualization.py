import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Project root
project_root = Path(__file__).resolve().parent.parent

# Load cleaned dataset
df = pd.read_csv(project_root / "data" / "processed" / "cleaned_sales.csv")

# Create reports/charts folder if it doesn't exist
charts_folder = project_root / "reports" / "charts"
charts_folder.mkdir(parents=True, exist_ok=True)

# -----------------------------
# 1. Sales by Category
# -----------------------------
category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8,5))
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig(charts_folder / "sales_by_category.png")
plt.close()

# -----------------------------
# 2. Top 10 Cities
# -----------------------------
city_sales = df.groupby("City")["Sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
city_sales.plot(kind="bar")
plt.title("Top 10 Cities by Sales")
plt.xlabel("City")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(charts_folder / "top10_cities.png")
plt.close()

# -----------------------------
# 3. Payment Methods
# -----------------------------
payment = df["Payment_Method"].value_counts()

plt.figure(figsize=(6,6))
payment.plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Payment Method Distribution")
plt.tight_layout()
plt.savefig(charts_folder / "payment_methods.png")
plt.close()

# -----------------------------
# 4. Monthly Sales Trend
# -----------------------------
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
monthly_sales = df.groupby(df["Order_Date"].dt.to_period("M"))["Sales"].sum()

plt.figure(figsize=(10,5))
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig(charts_folder / "monthly_sales.png")
plt.close()

print("Charts saved successfully!")
print("Location:", charts_folder)