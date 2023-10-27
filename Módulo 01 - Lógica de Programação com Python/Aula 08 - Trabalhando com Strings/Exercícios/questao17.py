import re

texto = """
Ricardo, cujo CPF é 123.456789-01, reuniu-se com Ana, cujo CPF é 987654.321-10, para discutir sobre o projeto.
Ambos discutiram sobre a proposta de Carlos, que tinha o CPF 456.123.78923, mas não puderam chegar a uma conclusão.
Eles decidiram agendar uma nova reunião para o próximo mês. Ana disse que também conversaria com seu colega João,
cujo CPF é 321.65498745, para obter uma perspectiva adicional. Esse é um CPF inválido: 321.123.1232-12.
"""

padrao_cpf = r'\d{3}\.\d{3}\.\d{3}-\d{2}'
cpfs_encontrados = re.findall(padrao_cpf, texto)

for cpf in cpfs_encontrados:
    cpf_numerico = re.sub(r'\D', '', cpf)
    if len(cpf_numerico) == 11:
        print(f"{cpf} é válido")