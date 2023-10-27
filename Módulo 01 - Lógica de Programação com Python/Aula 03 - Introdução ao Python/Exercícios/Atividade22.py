nome = input("Informe o nome do livro: ")
tempo_medio = int(input("Informe o tempo médio de leitura de uma página, em segundos: "))
tempo_leitura = int(input("Informe o tempo de leitura diário em segundos: "))
qtd_paginas = int(input("Informe a quantidade de páginas do livro: "))
qtd_paginas_dia = (tempo_leitura/tempo_medio)
tempo_ler_horas = (tempo_medio*qtd_paginas)/3600
tempo_ler_dias= qtd_paginas/qtd_paginas_dia
tempo_ler_semanas= tempo_ler_dias/7
print(f"Você leu {qtd_paginas_dia:.2f} páginas por dia, levou {tempo_ler_horas:.2f} horas para ler o livro, "
      f"{tempo_ler_dias:.2f} dias para ler o livro e {tempo_ler_semanas:.2f} semanas para ler o livro.")