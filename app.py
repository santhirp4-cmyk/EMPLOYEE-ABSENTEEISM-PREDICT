
import streamlit as st
import pandas as pd
import numpy as np

st.title("My First Streamlit App")
st.write("Welcome! This is my first Streamlit application.")

name = st.text_input("Enter your name")
if name:
    st.success(f"Hello {name} 👋")

number = st.slider("Pick a number", 0, 100, 25)
st.write("You picked:", number)

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)

st.line_chart(chart_data)


