texto = input("Digite um texto: ")
limite = int(input("Digite um limite de caracteres para o texto: "))

if len(texto) > limite:
    texto_limitado = texto [:limite] + "..."
    print(f"O texto limitado é: {texto_limitado}")
else:
    print(f"O texto é: {texto}")