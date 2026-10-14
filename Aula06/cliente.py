import joblib
import pandas as pd
import streamlit as st
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

MODELO_ARQUIVO = BASE_DIR / "modelo_titanic.joblib"

@st.cache_resource
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

st.subheader("Dados do Passageiro")
col1, col2 = st.columns(2)

with col1:
    classe = st.selectbox("Classe de Passagem: ", options=[1,2,3], index=2, format_func=lambda x: f"{x}a. Classe")