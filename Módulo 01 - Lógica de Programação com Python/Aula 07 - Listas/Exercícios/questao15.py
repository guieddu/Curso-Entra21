lista = [1, 1, 1, 2, 3, 3, 4, 4, 4, 4]

lista_comprimida = []
i = 0

while i < len(lista):
    elemento = lista[i]
    contador = 0

    while i < len(lista) and lista[i] == elemento:
        contador += 1
        i += 1

    if contador > 1:
        lista_comprimida.append((elemento, contador))
    else:
        lista_comprimida.append(elemento)

print(lista_comprimida)