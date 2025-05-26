import streamlit as st
import requests

st.title("Streamlit + FastAPI on AWS")

st.write("Enter some data to send to the API:")

name = st.text_input("Name")
value = st.number_input("Value", step=1.0)

if st.button("Submit to API"):
    payload = {"name": name, "value": value}
    try:
        res = requests.post("http://localhost:8000/predict/", json=payload)
        if res.status_code == 200:
            st.success(res.json())
        else:
            st.error(f"Error: {res.text}")
    except Exception as e:
        st.error(f"Failed to connect to API: {e}")
