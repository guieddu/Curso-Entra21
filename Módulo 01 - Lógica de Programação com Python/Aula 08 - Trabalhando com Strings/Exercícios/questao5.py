import re

texto = input("Digite o texto: ")

if re.search(r'\b(jequiti)|\b(curso de python)', texto):
    print("O texto é um SPAM")
else:
    print("O texto não é um SPAM")