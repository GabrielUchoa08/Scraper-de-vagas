import pandas as pd
from glob import glob

# encontrar todos os arquivos que batem com o padrão
arquivos = glob("data/raw/vagas_*.json")

# pegar o mais recente 
arquivos_ordenados = sorted(arquivos)
arquivo_mais_recente = arquivos_ordenados[-1]

print(f"Lendo arquivo: {arquivo_mais_recente}")

# le o JSON como DataFrame
df = pd.read_json(arquivo_mais_recente)

# extrair o nome da empresa de dentro do dicionário "company"
df["empresa"] = df["company"].apply(lambda c: c.get("display_name", "Não informado") if isinstance(c, dict) else "Não informado")

# extrair o nome do local de dentro do dicionário "location"
df["local"] = df["location"].apply(lambda loc: loc.get("display_name", "Não informado") if isinstance(loc, dict) else "Não informado")

# selecionar só as colunas que interessam pro projeto
colunas_interesse = [
    "id", "title", "empresa", "local", "salary_min", "salary_max",
    "description", "created", "area_busca", "termo_busca", "data_coleta", "redirect_url"
]

df_limpo = df[colunas_interesse]

# conferir o resultado
print(df_limpo.shape)
print(df_limpo.head())