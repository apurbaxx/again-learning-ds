import streamlit as st
import numpy as np
import pandas as pd

st.title("Hello Streamlit")

st.write("This is a simple text")

df = pd.DataFrame({
    "first column": [1,2,3,4],
    "second column": [10,20,30,40]
})

st.write("This is a sample data frame")
st.write(df)

#create a line chart of 20 rows and 3 columns
chart_data = pd.DataFrame(
    np.random.randn(20,3), columns=["a", "b", "c"]
)
st.line_chart(chart_data)

