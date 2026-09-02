SENIORIDADE = {
    "Júnior": [" jr ", " jr. ", "júnior", "junior"],
    "Pleno": ["pleno", " pl ", " pl. "],
    "Sênior": ["sênior", "senior", " sr ", " sr. "],
    "Especialista": ["especialista", " esp ", " esp. "]
}

def extrair_senioridade(titulo, senioridade_dict=SENIORIDADE):
    titulo = str(titulo).lower()

    for nivel, variacoes in senioridade_dict.items():
        if any(variacao in titulo for variacao in variacoes):
            return nivel

    return "Não especificado"