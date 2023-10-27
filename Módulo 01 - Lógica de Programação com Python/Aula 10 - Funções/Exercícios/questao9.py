def mostrar_informacoes(**kwargs):
    """
    Imprime informações no formato chave: valor
    """
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")