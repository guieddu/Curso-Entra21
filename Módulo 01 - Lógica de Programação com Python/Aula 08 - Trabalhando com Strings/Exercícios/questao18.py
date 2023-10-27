texto = """
Ricardo, cujo CPF é 123.456789-01, reuniu-se com Ana, cujo CPF é 987654.321-10, para discutir sobre o projeto.
Ambos discutiram sobre a proposta de Carlos, que tinha o CPF 456.123.78923, mas não puderam chegar a uma conclusão.
Eles decidiram agendar uma nova reunião para o próximo mês. Ana disse que também conversaria com seu colega João,
cujo CPF é 321.65498745, para obter uma perspectiva adicional. Esse é um CPF inválido: 321.123.1232-12.
"""

cpfs = []

i = 0
while i < len(texto):
    if texto[i].isdigit() and texto[i + 1].isdigit() and texto[i + 2].isdigit() and texto[i + 3] == '.' and texto[
        i + 4].isdigit() and texto[i + 5].isdigit() and texto[i + 6].isdigit() and texto[i + 7] == '.' and texto[
        i + 8].isdigit() and texto[i + 9].isdigit() and texto[i + 10] == '-' and texto[i + 11].isdigit() and texto[
        i + 12].isdigit():
        cpf = texto[i:i + 14]
        cpf_numerico = ''.join(filter(str.isdigit, cpf))

        if len(cpf_numerico) == 11:
            soma = 0
            for j in range(9):
                soma += int(cpf_numerico[j]) * (10 - j)

            resto = soma % 11
            if resto < 2:
                digito1 = 0
            else:
                digito1 = 11 - resto

            soma = 0
            for j in range(10):
                soma += int(cpf_numerico[j]) * (11 - j)

            resto = soma % 11
            if resto < 2:
                digito2 = 0
            else:
                digito2 = 11 - resto

            if int(cpf_numerico[9]) == digito1 and int(cpf_numerico[10]) == digito2:
                cpfs.append(cpf)

        i += 14
    else:
        i += 1

for cpf in cpfs:
    cpf_formatado = f"{cpf[:3]}.{cpf[4:7]}.{cpf[8:11]}-{cpf[12:]}"
    print(f"{cpf_formatado} é válido")