# -*- coding: utf-8 -*-
"""Untitled9.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DDY5c-vIJzXF_2XqNaGVR62W_a0wgk9k
"""

import streamlit as st
import pandas as pd

st.title("Aplicacion de analisis de datos")
uploaded_file = st.file_uploarder("subir archivo CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("primeras 5 filas del archivo")
    st.write(df.head())