vetor = [0] * 8

for i in range(8):
    vetor[i] = int(input(f"Digite o valor para a posição {i}: "))

while True:
    try:
        x = int(input("Digite o valor de X (0-7): "))
        y = int(input("Digite o valor de Y (0-7): "))

        if 0 <= x < 8 and 0 <= y < 8:
            break
        else:
            print("Valores de X e Y devem estar no intervalo de 0 a 7.")
    except ValueError:
        print("Por favor, digite valores numéricos para X e Y.")

soma = vetor[x] + vetor[y]

print(f"A soma dos valores nas posições {x} e {y} é: {soma}")