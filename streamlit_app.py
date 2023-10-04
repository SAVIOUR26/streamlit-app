import streamlit as st

# Title
st.title("My First Streamlit App")

# Text
st.write("This is a simple Streamlit app.")

# Adding a chart
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 20, 30, 40, 50]
})

st.line_chart(df)

# Adding a sidebar
st.sidebar.header("Sidebar")
st.sidebar.write("This is a sidebar.")
