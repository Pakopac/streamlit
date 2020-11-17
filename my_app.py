import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('datas/weatherAUS.csv')
value = st.number_input("nombre de colonnes", 0, 99999, 0)
if value > 0:
    st.write(df.head(value))

st.write(df.keys())
st.write(df.dtypes)
st.write(df.shape)
st.write(df.describe())

print(df.info())

fig, ax = plt.subplots(figsize=(10,10))
sns.heatmap(df.corr(), annot=True, ax=ax)
st.pyplot(fig)

labels = ['MinTemp','MaxTemp', 'Evaporation']
x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig2, ax = plt.subplots()
rects1 = ax.bar(x - width/2, [len(df["MinTemp"]), len(df["MaxTemp"]), df["Evaporation"].notnull().sum()], width)
st.pyplot(fig2)