import streamlit as st
import numpy as np
import pandas as pd

st.title("Learning")

name = st.text_input("Enter Your Name")
age = st.slider("Select your age", 0,100)

options = ["Python", "C++"]
choice = st.selectbox("Choose your favourite programming language", options)


if name:
    st.write(f"Hello {name}")

if age:
    st.write(f"Your age is {age}")

if choice:
    st.write(f"Your choice is {choice}")

data = {
    "Name": ["Apurba", "Rajeev", "Akshita"],
    "Age": [18,19,20],
    "City": ["Bangalore", "Kolkata", "Punjab"]
}

df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)