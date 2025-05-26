import csv
from logica import calcular_media, verificar_situacao

ARQUIVO = 'boletim.csv'

def carregar_alunos():
    alunos = []
    try:
        with open(ARQUIVO, mode='r', newline='', encoding='utf-8') as f:
            leitor = csv.DictReader(f)
            for linha in leitor:
                aluno = {
                    "nome": linha["nome"],
                    "nota1": float(linha["nota1"]),
                    "nota2": float(linha["nota2"]),
                    "media": float(linha["media"]),
                    "status": linha["status"]
                }
                alunos.append(aluno)
    except FileNotFoundError:
        # Se não existir o arquivo, retorna lista vazia
        pass
    return alunos

def adicionar_aluno(nome, nota1, nota2):
    media = calcular_media(nota1, nota2)
    status = verificar_situacao(media)

    aluno = {
        "nome": nome,
        "nota1": nota1,
        "nota2": nota2,
        "media": media,
        "status": status
    }

    with open(ARQUIVO, mode='a', newline='', encoding='utf-8') as f:
        escritor = csv.DictWriter(f, fieldnames=["nome", "nota1", "nota2", "media", "status"])
        # Se o arquivo está vazio, escreve o cabeçalho
        f.seek(0)
        if f.tell() == 0:
            escritor.writeheader()
        escritor.writerow(aluno)

def listar_alunos():
    return carregar_alunos()
