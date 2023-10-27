nome = input("Digite seu nome: ")

vogais = "AEIOUaeiou"
consoantes = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"

total_caracteres = len(nome)
quantidade_vogais = sum(1 for char in nome if char in vogais)
quantidade_consoantes = total_caracteres - quantidade_vogais

print(f"Total de caracteres: {total_caracteres}")
print(f"Quantidade de vogais: {quantidade_vogais}")
print(f"Quantidade de consoantes: {quantidade_consoantes}")