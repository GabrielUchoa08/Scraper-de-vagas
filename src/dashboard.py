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

with aba_comparativo:
    st.subheader("Top skills por área")
    st.caption("Compara todas as áreas. Respeita apenas o filtro de senioridade.")

    top_por_area = st.slider("Skills por área", min_value=3, max_value=10, value=5)

    # base: todas as áreas, só filtrando senioridade
    df_vagas_sen = df_vagas[df_vagas["senioridade"].isin(senioridades_selecionadas)]
    df_skills_sen = df_skills[df_skills["senioridade"].isin(senioridades_selecionadas)]

    if df_vagas_sen.empty:
        st.info("Nenhuma vaga para a senioridade selecionada.")
    else:
        # total de vagas de cada área (o denominador da porcentagem)
        total_por_area = df_vagas_sen.groupby("area_busca")["id"].nunique()

        # em quantas vagas cada skill aparece, por área
        skills_por_area = (
            df_skills_sen.groupby(["area_busca", "skills"])["id"]
            .nunique()
            .reset_index(name="vagas")
        )

        # porcentagem relativa ao total de vagas DA PRÓPRIA ÁREA
        skills_por_area["pct"] = (
            skills_por_area["vagas"]
            / skills_por_area["area_busca"].map(total_por_area)
            * 100
        )

        # mantém só as top N de cada área
        top = (
            skills_por_area.sort_values("pct", ascending=False)
            .groupby("area_busca")
            .head(top_por_area)
        )

        n_areas = skills_por_area["area_busca"].nunique()

        fig_comp = px.bar(
            top,
            x="pct",
            y="skills",
            color="area_busca",
            facet_row="area_busca",
            orientation="h",
            labels={"pct": "% das vagas", "skills": "", "area_busca": "Área"},
            facet_row_spacing=0.08,
            height=280 * n_areas,
        )
        fig_comp.update_yaxes(matches=None, showticklabels=True, categoryorder="total ascending")
        fig_comp.update_xaxes(matches=None, showticklabels=True)
        fig_comp.update_layout(showlegend=False)

        # "area_busca=Dados" -> "Dados"
        fig_comp.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))

        st.plotly_chart(fig_comp, use_container_width=True)