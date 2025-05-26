# app.py

import streamlit as st

st.title("My First Streamlit App")

name = st.text_input("Enter your name:")

if name:
    st.write(f"Hello, {name}! Welcome to your Streamlit app.")
