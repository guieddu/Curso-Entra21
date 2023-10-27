"""
1. Escreva uma função chamada compressao_string, que receba uma string como parâmetro e retorne a versão comprimida da mesma.

Exemplo:
Entrada: “AAABBBCCCCAA”
Saída: “A3B3C4A2”
"""

def compressao_string(string:str):
    '''
    Essa função recebe uma string como parâmetro e retorne a versão comprimida da mesma.
    '''
    comprimido = ""
    count = 1

    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            comprimido += string[i - 1] + str(count)
            count = 1

    comprimido += string[-1] + str(count)

    return comprimido

string_recebida = input("Digite a string a ser comprimida: ")

print(compressao_string(string_recebida.upper()))