# Step 1: Import Streamlit
import streamlit as st

# Step 2: Title of your app
st.title("My First Streamlit App")

# Step 3: Write a description
st.write("Hello! This is my first project using Streamlit.")

# Step 4: Get input from user
name = st.text_input("Enter your name:")

# Step 5: Display input
st.write("Hello,", name)

# Step 6: Create a button
if st.button("Click me"):
    st.write("You clicked the button!")
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

