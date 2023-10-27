entrada = input("Digite uma lista de elementos separados por espaço: ").split()
lista = [int(elemento) for elemento in entrada]

lista_sem_duplicatas = []

for elemento in lista:
    if elemento not in lista_sem_duplicatas:
        lista_sem_duplicatas.append(elemento)

print("Lista sem duplicatas:", lista_sem_duplicatas)