salario_mensal = float(input("Digite o salário do funcionário: "))
valor_metas_desempenho = float(input("Digite o valor das metas de desempenho atingida pelo funcionário: "))
valor_total_venda = float(input("Digite o valor total das metas de venda do funcionário: "))

if valor_metas_desempenho == valor_total_venda:
    bonus = salario_mensal * 0.2
    print(f"O bônus é de {bonus:.2f}% do salário anual.")
elif valor_metas_desempenho >= valor_total_venda / 2:
    bonus = salario_mensal * 0.1
    print(f"O bônus é de {bonus:.2f}% do salário anual.")
else:
    print("O funcionário não receberá bônus.")