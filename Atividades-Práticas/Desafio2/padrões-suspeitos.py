import re

def identificar_padroes_suspeitos(arquivo_log, padroes_suspeitos):
    try:
        with open(arquivo_log, 'r') as f:
            conteudo_log = f.read()
    except FileNotFoundError:
        return "Arquivo de log não encontrado."

    resultados = {}
    for padrao, descricao in padroes_suspeitos.items():
        ocorrencias = re.findall(padrao, conteudo_log)
        if ocorrencias:
            resultados[descricao] = ocorrencias

    return resultados

padroes = {
    r"falha de login \w+": "Falha de login",
    r"erro 500": "Erro interno do servidor",
}

padroes_encontrados = identificar_padroes_suspeitos("log_servidor.txt", padroes)
if padroes_encontrados:
    print("🚨 Padrões suspeitos encontrados:\n", padroes_encontrados)
else:
    print("✅ Nenhum padrão suspeito encontrado.")
