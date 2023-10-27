numero = float(input("Insira um número:"))

if numero > 0:
    inverso = 1 / numero
    print(f"O inverso do número é: {inverso:.2f}")
else:
    valor_absoluto = abs(numero)
    print(f"O valor absoluto do número é: {valor_absoluto:.2f}")