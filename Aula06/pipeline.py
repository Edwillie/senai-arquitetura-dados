import sqlite3
import pandas as pd

CSV_ORIGEM = "titanic.csv"
DB_NAME = "pipeline_titanic.db"

# Estrutura de conexão do banco

conexao = sqlite3.connect(DB_NAME)

#Criando a camada bronze

dfBronze = pd.read_csv(CSV_ORIGEM)
#print(dfBronze)

dfBronze.to_sql("camada_bronze",
               conexao,
               if_exists="replace",
               index=False 
                )

#Criando a camada prata

dfPrata = dfBronze.copy()

# Idade
dfPrata["Age"] = dfPrata["Age"].fillna(dfPrata["Age"].median())

# Embarque

dfPrata["Embarked"] = dfPrata["Embarked"] \
                    .fillna(dfPrata["Embarked"].mode()[0])

dfPrata.to_sql("camada_prata",
               conexao,
               if_exists="replace",
               index=False
               )

#print(dfPrata)

#Criando a camada ouro

colunasUteis = ["Survived","Pclass","Sex","Age","SibSp","Parch","Fare","Embarked"]
dfOuro = dfPrata[colunasUteis].copy()

dfOuro["Sex"] = dfOuro["Sex"].map({"male":0,"female":1})
dfOuro["Embarked"] = dfOuro["Embarked"].map({"S":0,"C":1, "Q":2})

dfOuro.to_sql("camada_ouro",
              conexao,
              if_exists="replace",
              index=True
)

taxaSobrevivencia = dfOuro["Survived"].mean()
print("A taxa de sobrevivencia foi de ",taxaSobrevivencia)
print(dfOuro.head(10))

conexao.close()
