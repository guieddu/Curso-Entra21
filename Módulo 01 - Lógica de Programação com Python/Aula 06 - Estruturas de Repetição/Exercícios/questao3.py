numero = int(input("Digite um número inteiro positivo:"))

if numero <= 0:
    print("Operação inválida, o número deve ser positivo.")
else:
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")