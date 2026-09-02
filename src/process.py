import pandas as pd
from glob import glob
from skills import extrair_skills
from senioridade import extrair_senioridade

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

df_limpo = df[colunas_interesse].copy()

# tratar descrições vazias/nulas antes de extrair skills
df_limpo["description"] = df_limpo["description"].fillna("")

# criar coluna nova com a lista de skills e senioridade encontradas em cada vaga
df_limpo["skills"] = df_limpo["description"].apply(extrair_skills)
df_limpo["senioridade"] = df_limpo["title"].apply(extrair_senioridade)

# transformar em formato long
df_skills = df_limpo.explode("skills")

# remover linhas onde a skill ficou nula 
df_skills = df_skills.dropna(subset=["skills"])

print(df_skills[["title", "skills"]].head(15))

# salvar os dois arquivos processados
df_limpo.to_csv("data/processed/vagas_processadas.csv", index=False)
df_skills.to_csv("data/processed/skills_processadas.csv", index=False)

print("Arquivos salvos em data/processed/")