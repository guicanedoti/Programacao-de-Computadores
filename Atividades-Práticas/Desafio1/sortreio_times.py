import random

times = ["Brasil", "Alemanha", "Argentina", "França", "Inglaterra", "Espanha"]
time1 = random.choice(times)
time2 = random.choice([t for t in times if t != time1])

print("🏆 Partida de Hoje:")
print(f"{time1} ⚽ x ⚽ {time2}")
