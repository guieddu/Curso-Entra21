numeros = []

for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    numeros.append(numero)

menor = min(numeros)
maior = max(numeros)

print(f"O menor número é: {menor}")
print(f"O maior número é: {maior}")