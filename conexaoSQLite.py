from sqlalchemy import create_engine
import pandas as pd

banco = "DW.sqlite"
url_conexao = f"sqlite://{banco}"

engine = create_engine(url_conexao)

#testar conexao

try:
    with engine.connect() as conexao:
        print("conectado")
except Exception as e:
        print(f"erro ao se conectar: {e}")


#fim da conexao

query = '''
    select * from *****
'''

df = pd.read_sql(query, engine)
print(df)