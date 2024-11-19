from sqlalchemy import create_engine
import pandas as pd

usuario = "postgres"
senha = "******"
host = "localhost"
porta = 5432
database = "pagila"

url_conexao = f"postgresql+psycopg2://{usuario}:{senha}@{host}:{porta}/{database}"

engine = create_engine(url_conexao)

#testar conexao

try:
    with engine.connect() as conexao:
        print("conectado")
except Exception as e:
        print(f"erro ao se conectar: {e}")

#fim da conexao

query = '''
    select * from actor
'''

df = pd.read_sql(query, engine)
print(df)