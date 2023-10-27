import re

while True:

    string = input("Informe um nome e sobrenome: ")

    padrao = r"^(\w+)\s(\w+)$"
    valido = re.search(padrao, string)
    if not valido:
        print("O texto informado não é um nome e sobrenome. Tente Novamente.")
        continue
    else:
        novo_texto = re.sub(valido.group(2), "#"*len(valido.group(2)), string)
        print(f"O nome completo com o sobrenome anonimatizado é: {novo_texto}")
        break
