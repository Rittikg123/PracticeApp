import streamlit as st
from databricks.sdk.runtime import spark

st.title("Claims Dashboard")

# Load data
df = spark.sql("SELECT * FROM gold_claims")
pdf = df.toPandas()

# =====================
# KPIs
# =====================

st.subheader("Summary Metrics")

total_billed = pdf["billed_amount"].sum()
total_paid = pdf["paid_amount"].sum()
total_outstanding = pdf["outstanding_amount"].sum()

col1, col2, col3 = st.columns(3)

col1.metric("Total Billed", f"${total_billed:,.0f}")
col2.metric("Total Paid", f"${total_paid:,.0f}")
col3.metric("Total Outstanding", f"${total_outstanding:,.0f}")

# =====================
# Table
# =====================

st.subheader("Claims Detail")
st.dataframe(pdf)
