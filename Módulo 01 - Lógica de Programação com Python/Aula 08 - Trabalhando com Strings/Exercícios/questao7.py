import re

string = input("Digite uma string: ")

if re.search(r'\d+', string):
    lista = re.findall(r'\d+', string)
    print(lista)
else:
    print("Não há números em sua string")