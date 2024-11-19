from sqlalchemy import create_engine
import pandas as pd

server= '**********'
database = 'DW'
username = '********'
password = '***********'
conexao = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server'

engine = create_engine(conexao)

#testando conexao

try:
    with engine.connect() as conexao:
        print("conectado")
except Exception as e: 
    print(f"erro ao se conectar: {e}")

#fim da conexao

query = 'select * from ******'

df = pd.read_sql(query, engine)
print(df)
