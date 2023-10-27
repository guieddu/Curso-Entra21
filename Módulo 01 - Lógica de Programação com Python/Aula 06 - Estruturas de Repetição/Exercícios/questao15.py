num_alunos = 5
notas_por_aluno = 3
turma_media = 0

for i in range(num_alunos):
    nome_aluno = input(f"Digite o nome do {i + 1}º aluno: ")
    media_aluno = 0

    for j in range(notas_por_aluno):
        nota = float(input(f"Digite a {j + 1}ª nota de {nome_aluno}: "))
        media_aluno += nota

    media_aluno /= notas_por_aluno
    turma_media += media_aluno

    print(f"A média de {nome_aluno} é: {media_aluno:.2f}\n")

turma_media /= num_alunos
print(f"A média da turma é: {turma_media:.2f}")