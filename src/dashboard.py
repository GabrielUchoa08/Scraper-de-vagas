import streamlit as st
import pandas as pd

st.title("Dashboard de Vagas de Emprego")

# carregar os CSVs processados
df_vagas = pd.read_csv("data/processed/vagas_processadas.csv")
df_skills = pd.read_csv("data/processed/skills_processadas.csv")

# mostrar algumas infos básicas, só pra confirmar que carregou certo
st.write(f"Total de vagas: {len(df_vagas)}")
st.write(f"Total de menções de skills: {len(df_skills)}")

# mostrar uma tabela simples com as primeiras linhas
st.write(df_vagas.head(10))

areas_disponiveis = df_skills["area_busca"].unique()

areas_selecionadas = st.multiselect(
       "Escolha a(s) área(s):",
       options=areas_disponiveis,
       default=areas_disponiveis  
   )

df_skills_filtrado = df_skills[df_skills["area_busca"].isin(areas_selecionadas)]

contagem_skills = df_skills_filtrado["skills"].value_counts()

st.subheader("Skills mais demandadas")

st.bar_chart(contagem_skills.head(15))