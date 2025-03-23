import sqlite3
import pandas as pd

# Nome do arquivo CSV e do banco SQLite
csv_file = "dataset_professora_predicoes.csv"  # Substitua pelo nome do seu arquivo CSV
sqlite_db = "banco_professora.db"  # Nome do banco de dados SQLite

# Conectar ao banco SQLite (se não existir, será criado)
conn = sqlite3.connect(sqlite_db)
cursor = conn.cursor()

# Carregar o CSV em um DataFrame Pandas
df = pd.read_csv(csv_file)

# Criar tabela automaticamente com base nas colunas do CSV
table_name = "feedbacks_predicao"

df.to_sql(table_name, conn, if_exists="replace", index=True)

# Verificar se os dados foram inseridos corretamente
print("Dados inseridos com sucesso! Exibindo 5 primeiras linhas:")
print(pd.read_sql(f"SELECT * FROM {table_name}", conn))

# Fechar conexão
conn.close()