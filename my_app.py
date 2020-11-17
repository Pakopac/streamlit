import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

#Récupère les csv du dossier data pour permettre le choix
st.markdown('## Choix du jeu de donnée', unsafe_allow_html=True)
base_path = '../datas/'

list_dataset = os.listdir(base_path)
options = list(range(len(list_dataset)))
path = st.selectbox("csv", options, format_func=lambda x: list_dataset[x])  

df = pd.read_csv(base_path + list_dataset[path])

#Afficher le nombre de colonnes demandées
st.markdown('## Choix du nombre de colonnes', unsafe_allow_html=True)
value = st.number_input("nombre de colonnes", 0, 99999, 0)
if value > 0:
    st.write(df.head(value))

# Bouttons qui affichent les infos
st.markdown('## Information du jeu de donnée', unsafe_allow_html=True)
if st.button('Nom des Colonnes'):
    st.write(df.keys())
if st.button('Type des Colonnes'):
    st.write(df.dtypes)
if st.button('Shape du Dataset'):
    st.write(df.shape)
if st.button('Statistiques Descriptives'):
    st.write(df.describe())

#Création du heatmap
st.markdown('## Choix des graphiques à afficher', unsafe_allow_html=True)
fig, ax = plt.subplots(figsize=(10,10))
sns.heatmap(df.corr(), annot=True, ax=ax)

#Checkbox pour afficher le heatmap
st.markdown('### Heatmap', unsafe_allow_html=True)
heatmap = st.checkbox('Heatmap')
if heatmap:
     st.pyplot(fig)

list_graph = ("barplot", "scatter")
options = list(range(len(list_graph)))
st.markdown('### Type de Graph', unsafe_allow_html=True)
choice_graph = st.selectbox("", options, format_func=lambda x: list_graph[x])  

st.markdown('### Taille des categories', unsafe_allow_html=True)
for i in range(df.shape[1]):
    if st.checkbox(df.columns[i]):
        labels = [df.columns[i]]
        x = np.arange(len(labels))
        width = 0.35
        if choice_graph == 0:
            fig2, ax = plt.subplots()
            rects1 = ax.bar(x - width/2, [df[df.columns[i]].notnull().sum()], width)
        elif choice_graph == 1:
            fig2 = plt.figure()
            sns.scatterplot(data=df[df.columns[i]])
        st.pyplot(fig2)