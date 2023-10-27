"""
Em python nós podemos utilizar o laço de repetição FOR para percorrer os elementos de um iterable.
"""

# Criando um Range
print(range(10))

# Como saber se um método é iterable
print(hasattr(range(10), "__iter__"))

# Utilizando o for para percorrer um range
# range(0, 10) -> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
for i in range(10):
    print(i, end=" ")  # Mostrar os prints na mesma linha

print()

for i in range(1, 10):
    print(i, end=" ")

print()

# Especificar o passo
for i in range(1, 10, 2):
    print(i, end=" ")

print()

# Quando o valor de i não é necessário
for _ in range(10):
    print("O código repetiu!")

print()

# Percorrendo inversamente
for i in range(10, 0, -1):
    print(i, end=" ")

print()

# Mostrar a quantidade de vezes que o código repetiu
for i in range(10):
    print(f"O código repetiu pela {i + 1}ª vez")

# For em JavaScript: for (let i = 0; i < 10; i++) {}
# for i in range(0, 10, 1):

