animais = {
    "gatos": "Miaw",
    "cachorros": 22,
    "zebra": 10,
    "girafa": 15,
    "panda": 23,
    "coala": 3
}

soma_valores = 0

for valor in animais.values():
    if isinstance(valor, int):
        soma_valores += valor

print("A soma dos valores numéricos é:", soma_valores)