import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv(r"C:\Users\KIIT0001\Desktop\Python\Scikit Learn\IRIS.csv")

# One frame (fig), two canvases (ax1, ax2)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

# Paint on the first canvas
sns.scatterplot(data=data, x="sepal_length", y="sepal_width", ax=ax1)
ax1.set_title("Sepal Dimensions")

# Paint on the second canvas
sns.scatterplot(data=data, x="petal_length", y="petal_width", ax=ax2)
ax2.set_title("Petal Dimensions")

st.pyplot(fig)

# 3. Your existing area chart
st.bar_chart(
    data, 
    y=["sepal_length", "sepal_width", "petal_length", "petal_width"], 
    color="species",
    height=600
)