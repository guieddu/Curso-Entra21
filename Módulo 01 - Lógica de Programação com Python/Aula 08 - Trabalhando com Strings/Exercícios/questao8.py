texto = input("Digite o texto: ")
palavra = input("Digite a palavra a ser verificada no texto: ")

if palavra in texto:
    vezes = texto.count(palavra)
    print(f"A palavra {palavra} aparece {vezes} vezes no texto")