import random
import string

def gerar_senha(comprimento=12, incluir_maiusculas=True, incluir_minusculas=True, incluir_numeros=True, incluir_simbolos=True):
    caracteres = ""
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        return "Selecione pelo menos um tipo de caractere."

    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

senha_gerada = gerar_senha()
print("Senha gerada:", senha_gerada)

senha_personalizada = gerar_senha(comprimento=16, incluir_simbolos=False)
print("Senha personalizada:", senha_personalizada)
