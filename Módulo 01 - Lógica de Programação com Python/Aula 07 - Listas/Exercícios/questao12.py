numeros = [-2, 3, 4, 0, 7, -1]

soma_consecutivos = 0
soma_temporaria = 0

for numero in numeros:
    if numero > 0:
        soma_temporaria += numero
    else:
        if soma_temporaria > soma_consecutivos:
            soma_consecutivos = soma_temporaria
        soma_temporaria = 0

if soma_temporaria > soma_consecutivos:
    soma_consecutivos = soma_temporaria

print("A soma dos números consecutivos maiores que zero é:", soma_consecutivos)