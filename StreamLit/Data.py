import streamlit as st
import pandas as pd
import numpy as np
dic={
    "svm":{
        "model Name":"SVM",
        "Param":[1,2,3]
    }

}

dt=pd.read_csv(r"C:\Users\KIIT0001\Desktop\Python\Scikit Learn\Social_Network_Ads.csv")
for mp,model in dic.items():
    print(model["model Name"])
    print("Model2",mp)
st.dataframe(dic)
