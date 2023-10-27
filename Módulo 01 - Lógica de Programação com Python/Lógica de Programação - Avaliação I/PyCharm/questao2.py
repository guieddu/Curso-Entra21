
operacao = (input("Insira a operação desejada, considerando (+, -, *, /, %, log):"))
numero1 = (int(input("Insira o primeiro número:")))
numero2 = (int(input("Insira o segundo número:")))

if operacao == "+":
    soma = numero1 + numero2
    print(f"O resultado da soma dos números inseridos é: {soma}")
elif operacao == "-":
    subtracao = numero1 - numero2
    print(f"O resultado da subtração dos números inseridos é: {subtracao}")
elif operacao == "*":
    multiplicacao = numero1 * numero2
    print(f"O resultado da multiplicação dos números inseridos é: {multiplicacao}")
elif operacao == "/":
    divisao = numero1 / numero2
    print(f"O resultado da divisão dos números inseridos é: {divisao}")
elif operacao == "%":
    porcentagem = (numero1 / numero2) * 100
    print(f"O resultado da porcentagem dos números inseridos é {porcentagem}")
elif operacao == "log":
    logaritmo = math.log(numero1, numero2)
    print(f"O resultado do logaritmo dos números inseridos é {logaritmo}")
else:
    print("Operação inválida")