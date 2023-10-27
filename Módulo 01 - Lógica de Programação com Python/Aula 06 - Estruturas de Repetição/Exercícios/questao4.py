soma = 0

while True:
    numero = int(input("Digite um número inteiro positivo ou (0/negativo para encerrar):"))

    if numero <= 0:
        break
    else:
        soma += numero
        print(f"A soma dos números digitados até agora é: {soma}")

print(f"A soma total dos números digitados é: {soma}")