numero_secreto = 42
tentativas = 0

print("Bem-vindo ao jogo de adivinhação!")

while True:
    tentativa = int(input("Digite um número entre 1 e 100: "))
    tentativas += 1

    if tentativa < numero_secreto:
        print("O número é maior. Tente novamente!")
    elif tentativa > numero_secreto:
        print("O número é menor. Tente novamente!")
    else:
        print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
        break