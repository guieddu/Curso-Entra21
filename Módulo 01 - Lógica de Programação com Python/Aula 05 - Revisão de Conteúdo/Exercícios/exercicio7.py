cigarros_por_dias = int(input("Digite a quantidade de cigarros fumados por dia: "))
anos_fumando = int(input("Digite a quantos anos você fuma: "))

total_cigarros = cigarros_por_dias * 365 * anos_fumando

perda_por_cigarro = total_cigarros * 11

para_dias = perda_por_cigarro / (60 * 24)

print(f"O fumante perdera {para_dias:.0f} dias de vida")