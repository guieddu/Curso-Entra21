texto = input("Digite o texto: ")

palavras = texto.split()

contagem = {}

for palavra in palavras:
    palavra = palavra.lower().strip('.,!?()[]{}:;\'"')

    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

print(contagem)