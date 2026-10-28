import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Radar de Skills", layout="wide")

@st.cache_data
def carregar_dados():
    vagas = pd.read_csv("data/processed/vagas_processadas.csv")
    skills = pd.read_csv("data/processed/skills_processadas.csv")
    return vagas, skills

df_vagas, df_skills = carregar_dados()

st.title("Dashboard de Vagas")

# filtro na barra lateral
st.sidebar.header("Filtros")

areas = sorted(df_vagas["area_busca"].unique())
senioridades = sorted(df_vagas["senioridade"].unique())

areas_selecionadas = st.sidebar.multiselect("Área", options=areas, default=areas)
senioridades_selecionadas = st.sidebar.multiselect(
    "Senioridade", options=senioridades, default=senioridades
)

df_vagas_filtrado = df_vagas[
    df_vagas["area_busca"].isin(areas_selecionadas)
    & df_vagas["senioridade"].isin(senioridades_selecionadas)
]
df_skills_filtrado = df_skills[
    df_skills["area_busca"].isin(areas_selecionadas)
    & df_skills["senioridade"].isin(senioridades_selecionadas)
]

# evita erro quando nada está selecionado
if df_vagas_filtrado.empty:
    st.warning("Nenhuma vaga com esses filtros. Ajuste a seleção na barra lateral.")
    st.stop()

# criação das KPIs
pct_com_senioridade = (df_vagas_filtrado["senioridade"] != "Não especificado").sum() / len(df_vagas_filtrado) * 100

col1, col2, col3, col4 = st.columns(4)
col1.metric("Vagas", len(df_vagas_filtrado))
col2.metric("Empresas", df_vagas_filtrado["empresa"].nunique())
col3.metric("Skills distintas", df_skills_filtrado["skills"].nunique())
col4.metric("Senioridade identificada", f"{pct_com_senioridade:.0f}%")

# separação das abas
aba_skills, aba_comparativo, aba_senioridade, aba_vagas = st.tabs(
    ["Skills", "Comparativo", "Senioridade", "Vagas"]
)
with aba_skills:
    st.subheader("Skills mais demandadas")

    top_n = st.slider("Quantas skills mostrar", min_value=5, max_value=30, value=15)

    total_vagas = df_vagas_filtrado["id"].nunique()
    st.caption(f"Base: {total_vagas} vagas")

    pct_skills = (
        df_skills_filtrado.groupby("skills")["id"].nunique()   # vagas distintas por skill
        / total_vagas * 100
    )
    pct_skills = pct_skills.sort_values(ascending=False).head(top_n).reset_index()
    pct_skills.columns = ["skill", "pct_vagas"]

    fig = px.bar(
        pct_skills,
        x="pct_vagas",
        y="skill",
        orientation="h",
        labels={"pct_vagas": "% das vagas", "skill": ""},
        text=pct_skills["pct_vagas"].round(1),
    )
    fig.update_layout(yaxis={"categoryorder": "total ascending"})

    st.plotly_chart(fig, use_container_width=True)