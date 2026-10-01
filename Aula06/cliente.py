import joblib
import pandas as pd
import streamlit as st

MODELO_ARQUIVO = "modelo_titanic.joblib"

@st.cache_reource
def carregar_modelo():
    pacote = joblib.load(MODELO_ARQUIVO)
    return pacote["modelo"], pacote["colunas"]

st.set_page_config(page_title="Titanic: Você sobreviveria?", page_icon="\U0001F6A2")