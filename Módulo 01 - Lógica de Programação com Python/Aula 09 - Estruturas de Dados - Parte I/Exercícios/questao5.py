matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f"Digite o valor para a posição [{i+1}][{j+1}]: "))

contador = 0

for i in range(3):
    for j in range(3):
        if matriz[i][j] > 10:
            contador += 1

print(f"A matriz possui {contador} valores maiores que 10.")