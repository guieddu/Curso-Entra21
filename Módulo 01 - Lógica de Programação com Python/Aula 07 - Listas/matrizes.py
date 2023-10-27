matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Acessandos os elementos da matriz
print(matriz[1][1])
print(matriz[2][2])

# Cadastrando os dados em uma matriz
nova_matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(f"Digite o valor [{i}][{j}] da matriz: ")))
    nova_matriz.append(linha)

print(nova_matriz)

# Mostra a matriz na tela
for linha in matriz:
    for coluna in linha:
        if coluna == 0:
            print("-", end=" ")
        elif coluna == 1:
            print("X", end=" ")
        else:
            print("O", end=" ")
        print(coluna, end=" ")
    print()

"""
-1 -1 -1
0  -1  0 
0  0   1

O O O
- O -
- - X



Jogador Atual: X
Digite a linha da jogada (0 - 2): 
Digite a coluna da jogada (0 - 2):

# Verificar se a jogada é válida
# Verificar se a partida acabou:
  - Jogador ganhou a partida:
     verificar se a diagonal principal (tabuleiro[0][0] + tabuleiro[1][1] + tabuleiro[2][2] == 3 or == -3 
     verificar a diagonal secundário (tabuleiro[0][2] + tabuleiro[1][1] + tabuleiro[2][0]
     verificar a soma de qualquer linha é igual a 3 or -3
     verificar a soma de qualquer coluna é igual a 3 or -3
    
  - Jogo empatou: 9 jogadas
"""

