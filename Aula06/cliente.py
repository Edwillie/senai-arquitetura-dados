import joblib
import pandas as pd
import streamlit as st

MODELO_ARQUIVO = "modelo_titanic.joblib"

@st.cache_reource
def carregar_modelo():
    pacote = joblib.load(MODELO_ARQUIVO)
    return pacote["modelo"], pacote["colunas"]

st.set_page_config(page_title="Titanic: Você sobreviveria?", page_icon="\U0001F6A2")
st.title("Você Sobreviveria ao Titanic?")
st.write("Preencha os dados como se fosse um passageiro do Titanic:")

try:
    modelo, colunas = carregar_modelo()
except FileNotFoundError:
    st.error("Arquivo não encontrado.")