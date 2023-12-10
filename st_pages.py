import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def table():
    st.markdown('## Data')
    st.markdown('[Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)')
    df = pd.read_csv("data/data.csv")
    st.dataframe(df)


def charts():
    st.markdown('## Correlation matrix')
    df = pd.read_csv("data/data.csv")
    
    corr_features = ["age", "hypertension" , "heart_disease", "avg_glucose_level", "bmi", "stroke"]
    corr_selection = st.multiselect("Select features", corr_features, corr_features[-3:])
    corr_matrix = df[corr_selection].corr()
    plt.figure(figsize=(12, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
    # st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()