n = int(input("Digite a quantidade de degraus da escada: "))

for i in range(1, n + 1):
    espacos = " " * (n - i)
    degraus = "#" * i
    print(espacos + degraus)