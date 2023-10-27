lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

lista_intercalada = []

for i in range(len(lista1)):
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[i])

print(lista_intercalada)