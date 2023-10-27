nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
nota3 = float(input("Digite a terceira nota do aluno: "))

lista = [nota1, nota2, nota3]

media = (lista[0] + lista[1] + lista[2]) / 3

print(f"A média do aluno é: {media:.1f}")