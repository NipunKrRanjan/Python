import streamlit as st
import numpy as np
cities=["Pune","Mumbai","Bangalore","Hyderabad"]
from datetime import date
# Define your range
min_date = date(1920, 1, 1)
max_date = date(2026, 12, 31)
def accepted():
    name=st.text_input("Enter your name")
    address=st.text_area("Enter your address")
    email=st.text_input("Enter your email")
    dob=st.date_input("Enter your DOB",min_value=min_date,max_value=max_date,value=min_date)
    Resume=st.file_uploader("Upload your Resume",type="pdf")
    if(st.checkbox("Are you Person With Disability")):
        st.checkbox("Do you want special serives?")
    choice=st.multiselect("Select your preffered job location",cities)
    if st.button("Submit Application"):
        st.success(f"Thank you, {name}! Your application has been submitted.")

st.header("""JOB APPLICATION FORM""")
accepted()
       