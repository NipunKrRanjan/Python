import streamlit as st
days=["Mon","Tue","Wed","Thrus","Fri","Sat","Sun"]
st.title("Hello")
day=st.selectbox("Select your day",days)
st.success(f"The day selected is {day}")