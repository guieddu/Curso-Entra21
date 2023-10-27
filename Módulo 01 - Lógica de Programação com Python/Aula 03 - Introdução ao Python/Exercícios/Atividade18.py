preco = float(input("Informe o preço do produto em R$: "))
desconto = float(input("Informe o desconto em percentual: "))
valor_desconto = preco*(desconto/100)
valor_pagar = preco-valor_desconto
print(f"O valor do desconto é R$ {valor_desconto:.2f} e o preço a pagar é R$ {valor_pagar:.2f}.")