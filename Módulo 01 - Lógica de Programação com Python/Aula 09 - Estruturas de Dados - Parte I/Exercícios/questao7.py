matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f"Digite o valor para a posição [{i+1}][{j+1}]: "))

valor_x = int(input("Digite o valor a ser buscado (X): "))

linha_encontrada = -1
coluna_encontrada = -1

for i in range(3):
    for j in range(3):
        if matriz[i][j] == valor_x:
            linha_encontrada = i
            coluna_encontrada = j

if linha_encontrada != -1 and coluna_encontrada != -1:
    print(f"O valor {valor_x} está na posição [{linha_encontrada+1}][{coluna_encontrada+1}].")
else:
    print("Não encontrado.")
