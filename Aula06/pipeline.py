import pandas as pd
import sqlite3

CSV_ORIGEM = "\\Aula06\\titanic.csv"
DB_NAME = "\\Aula06\\pipeline_titanic.db"

conexao = sqlite3.connect(DB_NAME)
dfBronze = pd.read_csv(CSV_ORIGEM)

dfBronze.to_sql("camada_bronze", conexao, if_exists="replace", index=False)
dfPrata = dfBronze.copy()

# Ajuste de dados - Idade
