dicionario = {
    "hello": "olá",
    "world": "mundo",
    "good": "bom",
    "morning": "manhã",
    "evening": "tarde",
}

texto_ingles = input("Digite o texto em inglês: ")

palavras = texto_ingles.split()

texto_traduzido = [dicionario.get(palavra, palavra) for palavra in palavras]

texto_traduzido = " ".join(texto_traduzido)

print("Texto Traduzido:", texto_traduzido)