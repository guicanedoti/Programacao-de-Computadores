import random

print("⚽ Bem-vindo ao Jogo de Chute a Gol!")
chute = int(input("Chute um número de 1 a 5: "))
gol = random.randint(1, 5)

if chute == gol:
    print("🎯 GOOOL! Você acertou o canto.")
else:
    print(f"😢 Defesa! O goleiro foi para o canto {gol}.")
