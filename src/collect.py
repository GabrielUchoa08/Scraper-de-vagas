import requests

#importando credencias da API
APP_ID = "1a779ec3"
APP_KEY = "cfbb58b9e0c9ff78b41109ef88f76ff8"

# url utilizada para pegar os dados da API da adzuna
url = "https://api.adzuna.com/v1/api/jobs/br/search/1"

# parametros da requisição GET
params = {
    "app_id": APP_ID,
    "app_key": APP_KEY,
    "results_per_page": 25,
    "what": "dados",
    "content-type": "application/json"
}

# requisição GET para a API da adzuna
response = requests.get(url, params=params)

# convertendo a resposta em JSON
data = response.json()

# resultado da requisição
print(data)