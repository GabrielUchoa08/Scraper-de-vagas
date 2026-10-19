from matching import compilar_dict

SENIORIDADE = {
    "Estágio": ["estágio", "estagiário", "estagiária", "trainee"],
    "Júnior": ["jr", "jr.", "júnior", "junior", "i"],
    "Pleno": ["pleno", "pl", "pl.", "ii"],
    "Sênior": ["sênior", "senior", "sr", "sr.", "iii"],
    "Especialista": ["especialista"],
}

PADROES_SENIORIDADE = compilar_dict(SENIORIDADE)

def extrair_senioridade(titulo):
    titulo = str(titulo).lower()
    for nivel, padroes in PADROES_SENIORIDADE.items():
        if any(p.search(titulo) for p in padroes):
            return nivel
    return "Não especificado"