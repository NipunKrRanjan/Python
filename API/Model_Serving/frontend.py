import streamlit as st
import requests
st.header("Prediction model for iris species identification",text_alignment="center")
API_URL = "http://127.0.0.1:8000/predict"

col1,col2=st.columns(2,border=True)
sep_length=col1.number_input("Enter Sepal Length")
sep_width=col2.number_input("Enter Sepal Width")

col3,col4=st.columns(2,border=True)
petal_length=col3.number_input("Enter petal length")
petal_width=col4.number_input("Enter petal width")

input_data={
    "sepal_length":sep_length,
    "sepal_width":sep_width,
    "petal_length":petal_length,
    "petal_width":petal_width
}

if(st.button("Predict Species")):
    try:
        response=requests.post(API_URL,json=input_data)
        if response.status_code==200:
            result=response.json()
            st.success(f"Predicted Species: **{result['Predicted Species'].upper()}**")
        else:
            st.error(f"Error:{response.status_code}")
    except:
        st.error("Cannot load server")