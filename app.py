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
