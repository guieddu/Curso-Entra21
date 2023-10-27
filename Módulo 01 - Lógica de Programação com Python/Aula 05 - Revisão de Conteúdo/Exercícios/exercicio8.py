velocidade = int(input("Digite a velocidade do carro em km/h: "))

if velocidade > 80:
    conta_multa = velocidade - 80
    multa = conta_multa * 5
    print(f"Você foi multado em R$ {multa} por ultrapassar o limite de velocidade")
else:
    print("Você está dentro do limite de velocidade permitido")