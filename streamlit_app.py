import streamlit as st
import pandas as pd

st.title(
    "Mutual Fund Analytics Dashboard"
)

scorecard = pd.read_csv(
    "reports/fund_scorecard.csv"
)

st.subheader(
    "Top Performing Funds"
)

st.dataframe(
    scorecard.head(10)
)

st.subheader(
    "Fund Score Distribution"
)

st.bar_chart(
    scorecard["fund_score"]
)