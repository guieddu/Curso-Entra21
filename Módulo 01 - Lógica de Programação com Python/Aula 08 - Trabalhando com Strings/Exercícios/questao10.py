texto = input("Digite um texto: ")
palavras = texto.lower().split()
palavras_unicas = []

for palavra in palavras:
    if palavras.count(palavra) == 1:
        palavras_unicas.append(palavra)

quantidade_unicas = len(palavras_unicas)

print(f"A quantidade de palavras únicas presente no texto é: {quantidade_unicas}")