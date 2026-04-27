import streamlit as st
import pandas as pd
import numpy as np
page_title=["Home","About Us","Education"]

#Adding a progress bar
import time
prg=st.progress(0)
for i in range(0,100):
    time.sleep(0.009)
    prg.progress(i+1)

pg=st.sidebar.selectbox("Navigation",page_title,index=0)
if(pg=="Home"):
    st.write("Home Page")
if(pg=="About Us"):
    st.write("About Us Page")
if(pg=="Education"):
    st.write("Education")