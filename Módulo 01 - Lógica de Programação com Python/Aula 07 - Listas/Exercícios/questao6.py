numeros = input("Digite uma lista de números separados por espaço: ").split()
numeros = [int(numero) for numero in numeros]

numeros_pares = [numero for numero in numeros if numero % 2 == 0]

if len(numeros_pares) > 0:
    media_pares = sum(numeros_pares) / len(numeros_pares)
    print("Média dos números pares:", media_pares)
else:
    print("Não há números pares na lista.")