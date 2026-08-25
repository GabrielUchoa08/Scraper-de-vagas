import streamlit as st
import pandas as pd

# título da página
st.title("Dashboard de Vagas de Emprego")

# carregar os CSVs processados
df_vagas = pd.read_csv("data/processed/vagas_processadas.csv")
df_skills = pd.read_csv("data/processed/skills_processadas.csv")

# mostrar algumas infos básicas, só pra confirmar que carregou certo
st.write(f"Total de vagas: {len(df_vagas)}")
st.write(f"Total de menções de skills: {len(df_skills)}")

# mostrar uma tabela simples com as primeiras linhas
st.write(df_vagas.head(10))

st.subheader("Skills mais demandadas")

contagem_skills = df_skills["skills"].value_counts()

st.bar_chart(contagem_skills.head(15))