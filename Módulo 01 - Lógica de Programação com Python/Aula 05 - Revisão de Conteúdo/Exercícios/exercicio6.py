dias = int(input("Digite os dias alugados do carro: "))
kms = int(input("Digite os kms rodados com o carro alugado: "))

calcd = dias * 60
calck = kms * 0.15

preco = calcd + calck

print(f"O preço total do aluguel do carro é: R$ {preco:.2f}")