import re

def compilar(variacao):
    #compila uma expressão regular para a variação, adicionando limites de palavra se necessário
    v = re.escape(variacao)
    ini = r"\b" if variacao[0].isalnum() else ""
    fim = r"\b" if variacao[-1].isalnum() else ""
    return re.compile(ini + v + fim)

def compilar_dict(dicionario):
    return {chave: [compilar(v) for v in vs] for chave, vs in dicionario.items()}