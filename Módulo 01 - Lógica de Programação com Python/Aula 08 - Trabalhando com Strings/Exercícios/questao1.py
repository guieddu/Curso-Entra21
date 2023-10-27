import re

while True:
    string = input("Digite a string: ")
    if re.match(r'^\d+$', string):
        print("Valor inválido")
    else:
        print(f"A string digitada é: {string}")
        break