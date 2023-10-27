nome_completo = input("Digite o seu nome completo: ")
nomes = nome_completo.split()

preposicoes = ["das", "dos", "da", "de", "do", "e"]

if len(nomes) < 3:
    nome_abreviado = ""
    for nome in nomes:
        nome_abreviado += nome[0].upper()
else:
    nomes_abreviados = [nomes[0]] + [nome[0].upper() + "." if nome not in preposicoes else nome for nome in nomes[1:-1]] + [nomes[-1]]
    nome_abreviado = " ".join(nomes_abreviados)

print(nome_abreviado)