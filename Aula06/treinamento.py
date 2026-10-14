import sqlite3
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DB_NAME = BASE_DIR / "pipeline_titanic.db"

MODELO_SAIDA = BASE_DIR / "modelo_titanic.joblib"

COLUNAS_ATRIBUTOS = ["Pclass",
                     "Sex",
                     "Age",
                     "SibSp",
                     "Parch",
                     "Fare",
                     "Embarked"]

COLUNA_ALVO = "Survived"

conexao = sqlite3.connect(DB_NAME)
df = pd.read_sql("SELECT * FROM camada_ouro", conexao)
conexao.close()

print(df)

X = df[COLUNAS_ATRIBUTOS]
Y = df[COLUNA_ALVO]

X_treino, X_teste, y_treino, y_teste = train_test_split(X,Y,test_size=0.2, random_state=42 , stratify=Y)

modelo = RandomForestClassifier(n_estimators= 300, max_depth=6, class_weight="balanced_subsample", random_state=42)

modelo.fit(X_treino,y_treino)

y_pred = modelo.predict(X_teste)

acuracia = accuracy_score(y_teste,y_pred)

print("Acurácia do modelo: ",acuracia)
print("Relatório de Classificação:")
print(classification_report(
    y_teste,y_pred,target_names=["Não sobreviveu","Sobreviveu"]
))

#Salvar o modelo
pacote = {
    "modelo":modelo,
    "colunas": COLUNAS_ATRIBUTOS
}

joblib.dump(pacote, MODELO_SAIDA)