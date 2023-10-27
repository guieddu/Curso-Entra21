numeros = input("Digite uma lista de números separados por espaço: ").split()
numeros = [int(numero) for numero in numeros]

numeros_unicos = []

for numero in numeros:
    if numeros.count(numero) == 1:
        numeros_unicos.append(numero)

print("Números únicos na lista:", numeros_unicos)