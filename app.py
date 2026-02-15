import streamlit as st
import pandas as pd

# Sample data (same as your gold_claims table)
data = {
    "claim_id": [1, 2, 3],
    "customer_name": ["Customer A", "Customer B", "Customer C"],
    "region": ["East", "West", "South"],
    "billed_amount": [5000, 3000, 2000],
    "paid_amount": [2000, 1000, 0],
    "outstanding_amount": [3000, 2000, 2000]
}

df = pd.DataFrame(data)

st.title("Claims Dashboard")

st.subheader("Summary Metrics")

total_billed = df["billed_amount"].sum()
total_paid = df["paid_amount"].sum()
total_outstanding = df["outstanding_amount"].sum()

col1, col2, col3 = st.columns(3)

col1.metric("Total Billed", f"${total_billed:,.0f}")
col2.metric("Total Paid", f"${total_paid:,.0f}")
col3.metric("Outstanding", f"${total_outstanding:,.0f}")

st.subheader("Claims Data")
st.dataframe(df)
