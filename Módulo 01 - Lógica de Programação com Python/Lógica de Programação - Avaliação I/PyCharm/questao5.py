valor = int(input("Digite o valor em reais: "))

notas100 = valor // 100
valor %= 100

notas50 = valor // 50
valor %= 50

notas10 = valor // 10
valor %= 10

notas5 = valor // 5
valor %= 5

notas2 = valor // 2
valor %= 2

moedas = valor

print("Quantidade de notas:")
print("Notas de 100 reais:", notas100)
print("Notas de 50 reais:", notas50)
print("Notas de 10 reais:", notas10)
print("Notas de 5 reais:", notas5)
print("Notas de 2 reais:", notas2)
print("Moedas de 1 real:", moedas)