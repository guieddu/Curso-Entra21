n = int(input("Digite o tamanho da matriz identidade: "))

matriz_identidade = [[0] * n for _ in range(n)]

for i in range(n):
    matriz_identidade[i][i] = 1

print("Matriz Identidade:")
for linha in matriz_identidade:
    print(linha)