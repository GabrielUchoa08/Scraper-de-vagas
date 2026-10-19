from matching import compilar_dict

SKILLS = {
    "Python": ["python"],
    "SQL": ["sql", "postgresql", "mysql", "sqlite"],
    "Machine Learning": ["machine learning", "ml", "aprendizado de máquina"],
    "Deep Learning": ["deep learning", "aprendizado profundo"],
    "R": [" r "," r.", "linguagem r"],
    "Pandas": ["pandas"],
    "Git": [" git ", " git.", " git,", "github"],
    "GCP": ["gcp", "google cloud platform"],
    "Excel": ["excel", "planilhas", "planilha"],
    "Power BI": ["power bi", "powerbi"],
    "AWS": ["aws", "amazon web services"],
    "Azure": ["azure", "microsoft azure"],
    "Docker": ["docker", "container"],
    "Kubernetes": ["kubernetes", "k8s"],
    "Google Ads": ["google ads"],
    "SEO": ["seo"],
    "JavaScript": ["javascript", " js "],
    "React": ["react", "react.js", "reactjs"],
    "Node.js": ["node.js", "nodejs", " node "],
    "TypeScript": ["typescript", " ts "],
    "Java": ["java"],
    "C#": ["c#", "c sharp"],
    "C++": ["c++", "cpp"],
    "PHP": ["php"],
    "Ruby": ["ruby", "ruby on rails", "rails"],
    "Go": [" go ", "golang"],
    "Swift": ["swift"],
    "Vue.js": ["vue.js", "vuejs", " vue "],
    "Angular": ["angular", "angular.js", "angularjs"],
    "Rest API": ["rest api", "api rest", "restful api"],
    "GraphQL": ["graphql"],
    "WordPress": ["wordpress", " wp "],
    "Copywriting": ["copywriting", "redação publicitária"],
    "Photoshop": ["photoshop", "adobe photoshop"],
    "Illustrator": ["illustrator", "adobe illustrator"],
    "InDesign": ["indesign", "adobe indesign"],
    "After Effects": ["after effects", "adobe after effects"],
    "Premiere Pro": ["premiere pro", "adobe premiere pro"],
    "Figma": ["figma"],
    ".Net": [".net", "dotnet"],
}

PADROES_SKILLS = compilar_dict(SKILLS)

#extraindo skills a partir do dicionário de skills
def extrair_skills(texto):
    texto = str(texto).lower()
    return [skill for skill, padroes in PADROES_SKILLS.items()
            if any(p.search(texto) for p in padroes)]