turno = input("Digite o turno em que você estuda, sendo (M) para MATUTINO, (V)\
 para VESPERTINO e (N) para NOTURNO:")

if turno == "M":
    print("Bom dia!")
elif turno == "V":
    print("Boa tarde!")
elif turno == "N":
    print("Boa noite!")
else:
    print("Valor inválido!")