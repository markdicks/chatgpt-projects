import streamlit as st
import pandas as pd
import numpy as np

st.title("Budget Calculator")

income = st.number_input("Income", value=0)
expense = st.number_input("Expense", value=0)

df = pd.DataFrame({
    "Income": [income],
    "Expense": [expense]
})

if st.button("Add"):
    df = pd.concat([df, pd.DataFrame({
        "Income": [income],
        "Expense": [expense]
    })], ignore_index=True)

if st.checkbox("Show Data"):
    st.write(df)

if st.button("Plot"):
    if df.empty:
        df = pd.DataFrame({
            "Income": [0],
            "Expense": [0]
        })
    df.plot.bar(rot=0)
    st.pyplot()

st.set_option('deprecation.showPyplotGlobalUse', False)
