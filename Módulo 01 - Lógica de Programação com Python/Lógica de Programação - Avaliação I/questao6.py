numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))
numero4 = int(input("Digite o quarto número: "))

min_numero = min(numero1, numero2, numero3, numero4)
max_numero = max(numero1, numero2, numero3, numero4)

soma = numero1 + numero2 + numero3 + numero4
num_meio1 = soma - min_numero - max_numero

min_numero2 = min(num_meio1, numero2, numero3, numero4)
max_numero2 = max(num_meio1, numero2, numero3, numero4)

print(min_numero2, min_numero, max_numero2, max_numero)





