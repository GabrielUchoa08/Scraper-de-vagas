import streamlit as st
import pandas as pd

st.title("Dashboard de Vagas de Emprego")

# carregar os CSVs processados
df_vagas = pd.read_csv("data/processed/vagas_processadas.csv")
df_skills = pd.read_csv("data/processed/skills_processadas.csv")

senioridades_disponiveis = df_vagas["senioridade"].unique()

# mostrar algumas infos básicas, só pra confirmar que carregou certo
st.write(f"Total de vagas: {len(df_vagas)}")

colunas_tabela = [
    "title",
    "empresa",
    "local",
    "senioridade",
    "area_busca",
    "redirect_url"
]

# mostrar uma tabela simples com as primeiras linhas
st.subheader("Vagas encontradas")
st.dataframe(
    df_vagas[colunas_tabela],
    use_container_width=True,
    hide_index=True
)
areas_disponiveis = df_skills["area_busca"].unique()

areas_selecionadas = st.multiselect(
       "Escolha a(s) área(s):",
       options=areas_disponiveis,
       default=areas_disponiveis  
   )

senioridades_selecionadas = st.multiselect(
    "Escolha a(s) senioridade(s):",
    options=senioridades_disponiveis,
    default=senioridades_disponiveis
)

df_vagas_filtrado = df_vagas[
    df_vagas["area_busca"].isin(areas_selecionadas)
    & df_vagas["senioridade"].isin(senioridades_selecionadas)
]

df_skills_filtrado = df_skills[
    df_skills["area_busca"].isin(areas_selecionadas)
    & df_skills["senioridade"].isin(senioridades_selecionadas)
]

contagem_skills = df_skills_filtrado["skills"].value_counts()

st.subheader("Skills mais demandadas")

st.bar_chart(contagem_skills.head(15))

st.subheader("Vagas por senioridade")

contagem_senioridade = (
    df_vagas_filtrado["senioridade"]
    .value_counts()
)

st.bar_chart(contagem_senioridade)