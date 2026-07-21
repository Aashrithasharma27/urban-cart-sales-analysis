import os
import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------
# Page Configuration
# -----------------------
st.set_page_config(
    page_title="Urban Cart Sales Dashboard",
    page_icon="🛒",
    layout="wide"
)

st.title("🛒 Urban Cart Sales Analysis Dashboard")
st.markdown("Interactive Sales Dashboard built using Python, Pandas, Plotly & Streamlit")

# -----------------------
# Load Data (cached + path-safe)
# -----------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "cleaned_sales.csv")


@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    data = pd.read_csv(path)
    data["Order_Date"] = pd.to_datetime(data["Order_Date"])
    return data


df = load_data(DATA_PATH)

# -----------------------
# Sidebar Filters
# -----------------------
st.sidebar.header("Filters")

category = st.sidebar.multiselect(
    "Select Category",
    options=sorted(df["Category"].unique()),
    default=sorted(df["Category"].unique())
)

city = st.sidebar.multiselect(
    "Select City",
    options=sorted(df["City"].unique()),
    default=sorted(df["City"].unique())
)

payment = st.sidebar.multiselect(
    "Payment Method",
    options=sorted(df["Payment_Method"].unique()),
    default=sorted(df["Payment_Method"].unique())
)

filtered_df = df[
    (df["Category"].isin(category)) &
    (df["City"].isin(city)) &
    (df["Payment_Method"].isin(payment))
]

# -----------------------
# Empty-filter guard
# -----------------------
if filtered_df.empty:
    st.warning("⚠️ No data matches the selected filters. Try adjusting your selection.")
    st.stop()

# -----------------------
# KPI Cards
# -----------------------
total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = filtered_df["Order_ID"].nunique()

col1, col2, col3 = st.columns(3)
col1.metric("💰 Total Sales", f"₹{total_sales:,.2f}")
col2.metric("📈 Total Profit", f"₹{total_profit:,.2f}")
col3.metric("🛍️ Total Orders", total_orders)

st.divider()

# -----------------------
# Sales by Category
# -----------------------
category_sales = (
    filtered_df.groupby("Category")["Sales"]
    .sum()
    .reset_index()
)

fig1 = px.bar(
    category_sales,
    x="Category",
    y="Sales",
    title="Sales by Category"
)
st.plotly_chart(fig1, width="stretch")

# -----------------------
# Top 10 Cities
# -----------------------
city_sales = (
    filtered_df.groupby("City")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig2 = px.bar(
    city_sales,
    x="City",
    y="Sales",
    title="Top 10 Cities by Sales"
)
st.plotly_chart(fig2, width="stretch")

# -----------------------
# Monthly Sales
# -----------------------
monthly = (
    filtered_df
    .groupby(filtered_df["Order_Date"].dt.to_period("M"))["Sales"]
    .sum()
)
monthly.index = monthly.index.astype(str)

fig3 = px.line(
    x=monthly.index,
    y=monthly.values,
    labels={"x": "Month", "y": "Sales"},
    title="Monthly Sales Trend"
)
st.plotly_chart(fig3, width="stretch")

# -----------------------
# Data Table
# -----------------------
st.subheader("Filtered Data")
st.dataframe(filtered_df)

csv = filtered_df.to_csv(index=False).encode("utf-8")
st.download_button(
    "⬇ Download Filtered Data",
    csv,
    file_name="filtered_sales.csv",
    mime="text/csv"
)
