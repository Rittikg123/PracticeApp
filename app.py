import streamlit as st
from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder.getOrCreate()

st.title("Claims Dashboard")

# Load table from Databricks
df = spark.sql("SELECT * FROM gold_claims")

# Convert to pandas for display
pdf = df.toPandas()

# =========================
# KPI SECTION
# =========================

st.subheader("Summary Metrics")

total_billed = pdf["billed_amount"].sum()
total_paid = pdf["paid_amount"].sum()
total_outstanding = pdf["outstanding_amount"].sum()

col1, col2, col3 = st.columns(3)

col1.metric("Total Billed", f"${total_billed:,.0f}")
col2.metric("Total Paid", f"${total_paid:,.0f}")
col3.metric("Total Outstanding", f"${total_outstanding:,.0f}")

# =========================
# FILTER SECTION
# =========================

st.subheader("Filter by Region")

regions = pdf["region"].unique()
selected_regions = st.multiselect("Select region(s):", regions, default=regions)

filtered_df = pdf[pdf["region"].isin(selected_regions)]

# =========================
# DATA TABLE
# =========================

st.subheader("Claims Detail")
st.dataframe(filtered_df)
