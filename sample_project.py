import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


st.header('Titanic Survaivability Analysis')
st.subheader('this is smaller')
st.write('A **short** explanation of the project.')

titanic_df = pd.read_csv('https://raw.githubusercontent.com/agconti/kaggle-titanic/master/data/train.csv')

st.write('The raw data:')
st.write(titanic_df)

st.subheader('Correlation matrix')
titanic_corr = titanic_df.corr()
fig, ax = plt.subplots(figsize=(10,6))
sns.heatmap(titanic_corr, annot=True, ax=ax)
st.write(fig)

st.subheader('Plots')
fig, ax = plt.subplots(figsize=(10,6))
titanic_df.Age.hist()
st.write(fig)


fig, ax = plt.subplots(figsize=(10,6))
titanic_df.Fare.hist()
st.write(fig)
