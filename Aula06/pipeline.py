import pandas as pd
import sqlite3

CSV_ORIGEM = "titanic.csv"
DB_NAME = "pipeline_titanic.db"

df = pd.read_csv(CSV_ORIGEM)

df.show()