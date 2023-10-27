import random

contadores = [0] * 6

for _ in range(100):
    resultado = random.randint(1, 6)
    contadores[resultado - 1] += 1

for i in range(6):
    print(f"Face {i + 1}: {contadores[i]} vezes")