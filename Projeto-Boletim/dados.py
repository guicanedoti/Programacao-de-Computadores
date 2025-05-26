alunos = []  # Nossa lista global para armazenar dados dos alunos

def adicionar_aluno(nome, nota1, nota2):
    from logica import calcular_media, verificar_situacao

    media = calcular_media(nota1, nota2)
    status = verificar_situacao(media)

    aluno = {
        "nome": nome,
        "nota1": nota1,
        "nota2": nota2,
        "media": media,
        "status": status
    }

    alunos.append(aluno)

def listar_alunos():
    return alunos
