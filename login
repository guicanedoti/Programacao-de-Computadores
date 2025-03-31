usuarios = {
    "usuario1": "senha123",
    "usuario2": "senha456",
    "usuario3": "senha789"
}

def verificar_login(usuario, senha):
    if usuario in usuarios and usuarios[usuario] == senha:
        return True
    else:
        return False

def sistema_login():
    tentativas = 3
    while tentativas > 0:
        usuario = input("Nome de usuário: ")
        senha = input("Senha: ")
        if verificar_login(usuario, senha):
            print("Login bem-sucedido!")
            return
        else:
            tentativas -= 1
            print(f"Login falhou. Tentativas restantes: {tentativas}")
    print("Número máximo de tentativas excedido. Conta bloqueada.")

sistema_login()
