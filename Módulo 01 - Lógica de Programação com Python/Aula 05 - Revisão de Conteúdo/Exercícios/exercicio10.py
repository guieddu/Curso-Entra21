valor_casa = float(input("Digite o valor da casa que você deseja comprar: "))
salario = float(input("Digite o seu salário: "))
anos_pagando = int(input("Digite a quantidade de anos que você levara para pagar: "))

meses_pagando = anos_pagando * 12
valor_prestacao = valor_casa / meses_pagando
limite_prestacao = salario * 0.30

if valor_prestacao <= limite_prestacao:
    print("Empréstimo aprovado!")
    print(f"Valor da prestação mensal: R$ {valor_prestacao:.2f}")
else:
    print("Empréstimo não aprovado, o valor da prestação excede 30% do salário.")