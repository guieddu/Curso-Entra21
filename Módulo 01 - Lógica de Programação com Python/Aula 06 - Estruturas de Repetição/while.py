"""
While não precisa de um iterable. Ele é utilizado quando não sabemos quantas
vezes o código irá repetir.
"""
i = 0

while i < 10:
    print(i, end=" ")
    i += 1

print()

# Laço de repetição infinito
# while True:
    # print("Repetiu")

# Exemplo de laço de repetição infinito
# Solicitar números até o usuário digitar um número negativo. Quando o usuário digitar um número negativo
# mostrar a soma dos números digitados.
"""
soma = 0
while True:
    numero = int(input("Digite um número: "))

    if numero <= 0:
        break

    soma += numero

print(f"A soma dos números digitados: {soma}")
"""

print()

# Mostrar todos os números pares de 0 à 100 utilizando o while
i = 0
while i <= 100:
    i += 1

    if i % 2 != 0:
        continue

    print(i, end=" ")


