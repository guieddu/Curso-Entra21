preco_x_burger = 10
preco_x_salada = 12
preco_x_bacon = 15
preco_x_tudo = 18

quantidade_x_burger = int(input("Digite a quantidade de X-Burger desejada: "))
quantidade_x_salada = int(input("Digite a quantidade de X-Salada desejada: "))
quantidade_x_bacon = int(input("Digite a quantidade de X-Bacon desejada: "))
quantidade_x_tudo = int(input("Digite a quantidade de X-Tudo desejada: "))

total_pedido = (preco_x_burger * quantidade_x_burger) + (preco_x_salada * quantidade_x_salada) + (preco_x_bacon * quantidade_x_bacon) + (preco_x_tudo * quantidade_x_tudo)

print(f"O valor total do pedido é: R${total_pedido}")