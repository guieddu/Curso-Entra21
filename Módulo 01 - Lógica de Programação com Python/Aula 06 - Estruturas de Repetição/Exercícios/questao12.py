fator1 = int(input("Digite o primeiro fator: "))
fator2 = int(input("Digite o segundo fator: "))

produto = 0
contador = 0

while contador < fator2:
    produto += fator1
    contador += 1

print(f"O produto de {fator1} e {fator2} é: {produto}")