import requests
import json
from datetime import date
import os
from dotenv import load_dotenv

load_dotenv()  

# credenciais da API
APP_ID = os.getenv("ADZUNA_APP_ID")
APP_KEY = os.getenv("ADZUNA_APP_KEY")

def buscar_vagas(termo, pagina=1):
    #busca vagas na API da Adzuna para um termo específico e retorna a lista de resultados
    url = f"https://api.adzuna.com/v1/api/jobs/br/search/{pagina}"

    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "results_per_page": 25,
        "what": termo,
        "content-type": "application/json"
    }

    response = requests.get(url, params=params)
    data = response.json()

    #retornando a lista de vagas 
    return data["results"]  

# lista de termos de busca organizados por área
termos_busca = {
    "Dados": ["cientista de dados", "analista de dados", "engenheiro de dados"],
    "Tech": ["desenvolvedor", "devops"],
    "Marketing": ["analista de marketing", "marketing digital"]
}

# data de hoje, antes do loop
data_hoje = date.today().isoformat()

# lista que vai acumular todas as vagas encontradas
todas_vagas = []

# percorre cada área e sua lista de termos
for area, termos in termos_busca.items():

    # percorre cada termo dentro daquela área
    for termo in termos:

        vagas_do_termo = buscar_vagas(termo)

        # marcar de qual área, termo e data essa vaga veio
        for vaga in vagas_do_termo:
            vaga["termo_busca"] = termo
            vaga["area_busca"] = area
            vaga["data_coleta"] = data_hoje

        todas_vagas.extend(vagas_do_termo)

caminho_arquivo = f"data/raw/vagas_{data_hoje}.json"

with open(caminho_arquivo, "w", encoding="utf-8") as f:
    json.dump(todas_vagas, f, ensure_ascii=False, indent=2)

print(f"Arquivo salvo em: {caminho_arquivo}")