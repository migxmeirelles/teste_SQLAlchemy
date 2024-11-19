from sqlalchemy import create_engine
import pandas as pd

usuario = "********"
senha = "**********"
host = "**********"
porta = 1521
sid = "******" 

url_conexao = (
   f"oracle+oracledb://{usuario}:{senha}@(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)"
   f"(HOST={host})(PORT={porta}))(CONNECT_DATA=(SID={sid})))"
)

engine = create_engine(url_conexao)

#testando conexao

try:
    with engine.connect() as conexao:
        print("conectado")
except Exception as e:
        print(f"Erro ao conectar: {e}")

#fim da conexao


query = '''
    select * from ******
'''

df = pd.read_sql(query, engine)
print(df)