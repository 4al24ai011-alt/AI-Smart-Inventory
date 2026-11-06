import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="AI Smart Inventory",
    page_icon="📦",
    layout="wide"
)

# Main heading
st.title("📦 AI-Powered Smart Inventory")
st.subheader("Inventory Management and Demand Prediction System")

st.write("Monitor product stock and understand inventory levels.")

# Sample inventory data
data = {
    "Product": ["Rice", "Wheat", "Sugar", "Oil", "Milk", "Coffee"],
    "Current Stock": [100, 50, 15, 40, 10, 60],
    "Daily Sales": [20, 10, 8, 5, 15, 6],
    "Price": [50, 40, 45, 120, 30, 150]
}

df = pd.DataFrame(data)

# Dashboard metrics
total_products = len(df)
total_stock = df["Current Stock"].sum()
low_stock = len(df[df["Current Stock"] <= 20])

col1, col2, col3 = st.columns(3)

col1.metric("Total Products", total_products)
col2.metric("Total Available Stock", total_stock)
col3.metric("Low Stock Products", low_stock)

st.divider()

# Inventory table
st.header("📋 Inventory Details")
st.dataframe(df, use_container_width=True)

# Low stock alerts
st.header("⚠️ Low Stock Alerts")

low_stock_df = df[df["Current Stock"] <= 20]

if not low_stock_df.empty:
    st.warning("Some products have low stock. Please consider restocking.")

    st.dataframe(
        low_stock_df[["Product", "Current Stock"]],
        use_container_width=True
    )
else:
    st.success("All products have sufficient stock.")

# Stock chart
st.header("📊 Product Stock Analysis")

chart_data = df.set_index("Product")[["Current Stock"]]

st.bar_chart(chart_data)

# Product information
st.header("🔍 Check Product Details")

selected_product = st.selectbox(
    "Select a product",
    df["Product"]
)

product = df[df["Product"] == selected_product].iloc[0]

st.write("Product:", product["Product"])
st.write("Available Stock:", product["Current Stock"])
st.write("Daily Sales:", product["Daily Sales"])
st.write("Price: ₹", product["Price"])

st.divider()

st.info(
    "AI Demand Prediction will be added in the next development stage."
)

st.caption("AI Smart Inventory Management System | Hackathon Project")