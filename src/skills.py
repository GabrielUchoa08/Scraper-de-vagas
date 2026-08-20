SKILLS = {
    "Python": ["python"],
    "SQL": ["sql", "postgresql", "mysql", "sqlite"],
    "Machine Learning": ["machine learning", "ml", "aprendizado de máquina"],
    "Deep Learning": ["deep learning", "aprendizado profundo"],
    "R": [" r "," r. ", "linguagem r"],
    "Pandas": ["pandas"],
    "Git": ["git", "github"],
    "GCP": ["gcp", "google cloud platform"],
    "Excel": ["excel", "planilhas", "planilha"],
    "Power BI": ["power bi", "powerbi"],
    "AWS": ["aws", "amazon web services"],
    "Azure": ["azure", "microsoft azure"],
    "Docker": ["docker", "container"],
    "Kubernetes": ["kubernetes", "k8s"],
    "Google Ads": ["google ads"],
    "SEO": ["seo"]
}

#extraindo skills a partir do dicionário de skills
def extrair_skills(texto, skills_dict=SKILLS):
    texto = texto.lower()  

    skills_encontradas = []

    for skill, variacoes in skills_dict.items():
        if any(variacao in texto for variacao in variacoes):
            skills_encontradas.append(skill)

    return skills_encontradas