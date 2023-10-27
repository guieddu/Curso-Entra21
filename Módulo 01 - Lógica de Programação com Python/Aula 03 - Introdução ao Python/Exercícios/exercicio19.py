nome = input("Digite o nome do vendedor:")
salario_fixo = int(input("Digite o salário fixo do vendedor:"))
vendas_mes = int(input("Digite o total de vendas efetuadas no mês (em dinheiro):"))

recebimento = 0.15 * vendas_mes

print(f"O total que o vendedor deve receber no mêS por suas comissões é: {recebimento:.2f}")

