x = int(input("Digite o valor de x: "))
n = int(input("Digite o valor de n: "))

resultado = 1

contador = 0
while contador < n:
    resultado *= x
    contador += 1

print(f"{x} elevado a {n} é igual a: {resultado}")