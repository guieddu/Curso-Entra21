lista1 = input("Digite a primeira lista separada por espaços: ").split()
lista2 = input("Digite a segunda lista separada por espaços: ").split()

set1 = set(lista1)
set2 = set(lista2)
intersecao = set1.intersection(set2)
elementos_comuns = list(intersecao)

print("Elementos em comum: ", elementos_comuns)