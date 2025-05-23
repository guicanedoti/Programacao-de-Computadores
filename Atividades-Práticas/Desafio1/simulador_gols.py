import random

time1 = input("Digite o nome do time 1: ")
time2 = input("Digite o nome do time 2: ")

gols_time1 = random.randint(0, 5)
gols_time2 = random.randint(0, 5)

print(f"\nResultado Final:")
print(f"{time1} {gols_time1} x {gols_time2} {time2}")
