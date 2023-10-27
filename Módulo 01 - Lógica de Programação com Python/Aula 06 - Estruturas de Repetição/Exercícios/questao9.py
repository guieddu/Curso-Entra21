valor_inicial = int(input("Digite o valor inicial do intervalo: "))
valor_final = int(input("Digite o valor final do intervalo: "))

numeros_pares = False

print("Números pares no intervalo:")

for numero in range(valor_inicial, valor_final + 1):
    if numero % 2 == 0:
        print(numero)
        numeros_pares = True

if not numeros_pares:
    print("O intervalo não possuí números pares")