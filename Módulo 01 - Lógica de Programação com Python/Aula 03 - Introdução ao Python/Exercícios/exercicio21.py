montante_inicial = float(input("Digite o montante incial do investimento:"))
taxa_juros = float(input("Digite a taxa de juros em porcentagem que possuirá sobre o investimento a.a:"))
tempo = float(input("Digite o período de tempo do investimento (anual):"))

valor_futuro = montante_inicial * (1 + taxa_juros/100) ** tempo

print (f"O valor futuro do investimento será: {valor_futuro:.2f}")