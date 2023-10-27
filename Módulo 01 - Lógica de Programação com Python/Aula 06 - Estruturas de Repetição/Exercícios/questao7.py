numero = int(input("Digite um número inteiro positivo:"))
soma = 0

if numero <= 0:
    print("Operação inválida, o número deve ser positivo.")
else:
    while numero > 0:
        digitos = numero % 10
        soma += digitos
        numero //= 10

    print(f"A soma dos dois dígitos é: {soma}")