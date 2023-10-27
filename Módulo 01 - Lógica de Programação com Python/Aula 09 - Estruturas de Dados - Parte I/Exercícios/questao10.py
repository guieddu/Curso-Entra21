pessoas = []

while True:
    nome = input("Digite o nome da pessoa (ou 'sair' para encerrar): ")

    if nome.lower() == 'sair':
        break

    cpf = input("Digite o CPF da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))

    pessoa = {
        "Nome": nome,
        "CPF": cpf,
        "Idade": idade
    }

    pessoas.append(pessoa)

maiores_idade = []
menores_idade = []

for pessoa in pessoas:
    if pessoa["Idade"] >= 18:
        maiores_idade.append(pessoa)
    else:
        menores_idade.append(pessoa)

print("\nPessoas maiores de idade:")
for pessoa in maiores_idade:
    print(f"Nome: {pessoa['Nome']}, CPF: {pessoa['CPF']}, Idade: {pessoa['Idade']}")

print("\nPessoas menores de idade:")
for pessoa in menores_idade:
    print(f"Nome: {pessoa['Nome']}, CPF: {pessoa['CPF']}, Idade: {pessoa['Idade']}")
