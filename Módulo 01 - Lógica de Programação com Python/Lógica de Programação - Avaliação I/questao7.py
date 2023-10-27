ano = int(input("Digite o ano: "))
mes = int(input("Digite o mês: "))
dia = int(input("Digite o dia: "))


if 1582 <= ano <= 2023:
    if 1 <= mes <= 12:
        if 1 <= dia <= 31:
            print("A data é válida")
        else:
            print("Data inválida")
    else:
        print("Data inválida")
else:
    print("Data inválida")
