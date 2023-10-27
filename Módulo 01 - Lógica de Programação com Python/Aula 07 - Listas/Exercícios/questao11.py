numeros = input("Digite uma lista de números inteiros separados por espaço: ").split()
numeros = [int(numero) for numero in numeros]

numeros_ordenados = sorted(numeros)

print("Números em ordem crescente:", numeros_ordenados)