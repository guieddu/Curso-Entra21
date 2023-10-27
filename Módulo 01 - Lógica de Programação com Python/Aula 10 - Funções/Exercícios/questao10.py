def formata_cpf(numero):
    numero_str = str(numero)
    if len(numero_str) != 11:
        return numero_str

    cpf_formatado = f"{numero_str[:3]}.{numero_str[3:6]}.{numero_str[6:9]}-{numero_str[9:11]}"
    return cpf_formatado

cpf_formatado = formata_cpf(12345678901)
print(cpf_formatado)

cpf_formatado2 = formata_cpf(12345)
print(cpf_formatado2)