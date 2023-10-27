dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))

quociente = 0

while dividendo >= divisor:
    dividendo -= divisor
    quociente += 1

print(f"O quociente da divisão de {dividendo} por {divisor} é: {quociente}")
