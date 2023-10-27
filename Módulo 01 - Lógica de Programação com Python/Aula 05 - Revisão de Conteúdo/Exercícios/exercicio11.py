consumo = float(input("Digite a quantidade de kWh consumida: "))
tipo = input("Digite o tipo de instalação (R para residencial, C para comercial, I para industrial): ").upper()

if tipo == 'R':
    if consumo <= 500:
        preco = consumo * 0.40
    else:
        preco = consumo * 0.65
elif tipo == 'C':
    if consumo <= 1000:
        preco = consumo * 0.55
    else:
        preco = consumo * 0.60
elif tipo == 'I':
    if consumo <= 5000:
        preco = consumo * 0.55
    else:
        preco = consumo * 0.60
else:
    preco = 0

if preco == 0:
    print("Tipo de instalação inválido.")
else:
    print(f"O preço a pagar é R$ {preco:.2f}")