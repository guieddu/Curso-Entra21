import random

palavras = ["python", "programacao", "computador", "desenvolvimento", "inteligencia", "artificial"]
palavra = random.choice(palavras)

letras_corretas = []
tentativas_maximas = 6
tentativas = 0

while True:
    palavra_oculta = ""
    for letra in palavra:
        if letra in letras_corretas:
            palavra_oculta += letra
        else:
            palavra_oculta += "_"

    print("\nPalavra: ", palavra_oculta)
    print("Tentativas restantes: ", tentativas_maximas - tentativas)

    if palavra_oculta == palavra:
        print("\nParabéns! Você adivinhou a palavra correta:", palavra)
        break

    if tentativas == tentativas_maximas:
        print("\nVocê esgotou todas as tentativas. A palavra correta era:", palavra)
        break

    letra_tentativa = input("\nDigite uma letra: ").lower()

    if len(letra_tentativa) != 1 or not letra_tentativa.isalpha():
        print("Por favor, insira uma única letra válida.")
        continue

    if letra_tentativa in letras_corretas:
        print("Você já tentou essa letra antes. Tente outra.")
        continue

    if letra_tentativa in palavra:
        letras_corretas.append(letra_tentativa)
        print("Letra correta!")
    else:
        tentativas += 1
        print("Letra incorreta!")