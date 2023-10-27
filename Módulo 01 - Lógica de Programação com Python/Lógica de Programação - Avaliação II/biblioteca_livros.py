def adicionar_livro(id: int, titulo: str, autor: str, ano: int, genero: str) -> None:  # 1
    """    Essa função adiciona o livro e seus dados a biblioteca"""
    livro = {
        'titulo': titulo,
        'autor': autor,
        'ano': ano,
        'genero': genero,
        'status': "Disponível",
        'avaliações': []
    }
    biblioteca[id] = livro
    input("Livro adicionado com sucesso! Pressione qualquer tecla para retornar ao Menu.")
    return


def remover_livro(id: int) -> None:  # 2
    """Essa função remove o livro da biblioteca"""
    if id in biblioteca.keys():
        del biblioteca[id]
        input(f"O livro com a ID {id} foi removido da biblioteca. Digite qualquer tecla para retornar ao Menu")
        return
    input("Não é possível remover um livro que não existe. Digite qualquer tecla para retornar ao Menu.")
    return


def emprestar_livro(id: int) -> None:  # 3
    """Empresta um livro da biblioteca, fazendo seu status ficar como 'Emprestado'"""
    biblioteca[id]["status"] = "Emprestado"
    input("Livro emprestado com sucesso!")
    return


def devolver_livro(id: int) -> None:  # 4
    """Devolve o livro à biblioteca, fazendo seu status ficar como 'Disponível'"""
    biblioteca[id]["status"] = "Disponível"
    input("Livro devolvido com sucesso!")
    return


def listar_livros() -> None:  # 5
    """Listar livros da biblioteca"""
    print("")
    for i in biblioteca:
        print(f"Livro {i}: Título: {biblioteca[i]['titulo']} | Autor: {biblioteca[i]['autor']} |"
              f" Ano: {biblioteca[i]['ano']} | Gênero: {biblioteca[i]['genero']} | Status: {biblioteca[i]['status']}")
    input("\nDigite qualquer tecla para retornar ao Menu.")

def buscar_livro(titulo: str) -> None:  # 6
    """Buscar livro pelo título"""

    for i in biblioteca:
        if biblioteca[i]["titulo"].upper() == titulo:
            print(
                f"Livro {i}: Título: {biblioteca[i]['titulo']} | Autor: {biblioteca[i]['autor']} |"
                f" Ano: {biblioteca[i]['ano']} | Gênero: {biblioteca[i]['genero']} | Status: {biblioteca[i]['status']}")
            input("Digite qualquer tecla para retornar ao Menu.")
            return
    input("Livro não encontrado! Digite qualquer tecla para retornar ao Menu.")
    return


def livros_por_autor(autor: str) -> None:  # 7
    """Informa todos os livros escritos pelo autor informado."""
    total_livros = 0
    print()
    for i in biblioteca:
        if biblioteca[i]["autor"].upper() == autor:
            print(f"Livro {i}: {biblioteca[i]['titulo']}")
            total_livros += 1
    if total_livros == 0:
        print("Não foi encontrado nenhum livro do autor informado!")
    return


def livros_por_genero(genero: str) -> None:  # 8
    """Informa todos os livros do gênero informado."""
    total_livros = 0
    print()
    for i in biblioteca:
        if biblioteca[i]["genero"].upper() == genero:
            print(f"Livro {i}: {biblioteca[i]['titulo']}")
            total_livros += 1
    if total_livros == 0:
        print("Não foi encontrado nenhum livro do gênero informado!")
    return


def livros_emprestado() -> None:  # 9
    """Imprime em cada linha o livro e seu status"""
    print("Relação de livros emprestados: ")
    qtd_emprestados = 0
    for id in biblioteca:
        if biblioteca[id]["status"] == "Emprestado":
            print(f'Livro {id}: "{biblioteca[id]["titulo"]}"')
            qtd_emprestados += 1
    if qtd_emprestados == 0:
        print("\nTodos os livros estão disponíveis!")
    return


def avaliar_livro(id: int) -> None:  # 10
    """Recebe o ID do livro como argumento, pede pelo valor da avaliação, depois adiciona a um array
              e pergunta se quer realizar uma nova adição no mesmo livro"""
    if id not in biblioteca.keys():
        input(f"O livro de ID {id} não foi encontrado! Digite qualquer tecla para retornar ao Menu.")
        return
    while True:
        d = int(input(f'De 1 a 5, dê a avaliação do livro {biblioteca[id]["titulo"]}: '))  # Pede pela avaliação.
        if d < 1 or d > 5:
            input("A sua nota deve ser de 1 a 5! Digite qualquer tecla para refazar a avaliação.")
            continue
        biblioteca[id]["avaliações"].append(d)  # Adiciona o valor à key como uma lista.
        continuar = input("Avaliação registrada com sucesso! Deseja fazer outra avaliação? (S/N)")
        if continuar.upper() != "S":
            break
    return


def obter_media_avaliacoes(id: int) -> None:  # 11
    """Obtém a média das avaliações do livro informado."""
    if id not in biblioteca.keys():
        input(f"O livro de ID {id} não foi encontrado! Digite qualquer tecla para retornar ao Menu.")
        return

    """Faz a soma de todos os itens da lista "avaliações" e a soma é divida
     pelo tamanho desta mesma lista, assim tendo a média."""

    media = sum(biblioteca[id]["avaliações"]) / len(biblioteca[id]["avaliações"])
    input(f"\nA média das avaliações do livro {(biblioteca[id]['titulo'])} é {media:.2f}.\n"
          f"Digite qualquer tecla para retornar ao Menu.")
    return


biblioteca = {
    1: {"titulo": "Cem Anos de Solidão", "autor": "Gabriel García Márquez", "ano": 1967, "genero": "Realismo Mágico",
        "status": "Emprestado", "avaliações": [5, 4, 4, 3, 4]},
    2: {"titulo": "Dom Quixote", "autor": "Miguel de Cervantes", "ano": 1605, "genero": "Romance",
        "status": "Emprestado", "avaliações": [3, 1, 2, 4, 2]},
    3: {"titulo": "Orgulho e Preconceito", "autor": "Jane Austen", "ano": 1813, "genero": "Romance Clássico",
        "status": "Disponível", "avaliações": [3, 3, 5, 2, 4]},
    4: {"titulo": "Ulisses", "autor": "James Joyce", "ano": 1922, "genero": "Modernismo", "status": "Emprestado",
        "avaliações": [1, 1, 1, 1, 4]},
    5: {"titulo": "O Apanhador no Campo de Centeio", "autor": "J.D. Salinger", "ano": 1951,
        "genero": "Ficção Adolescente", "status": "Emprestado", "avaliações": [3, 4, 4, 1, 2]},
    47: {"titulo": "1984", "autor": "Hermann Hesse", "ano": 1927, "genero": "Ficção Filosófica",
         "status": "Emprestado", "avaliações": [2, 3, 4, 2, 3]}
}

while True:
    print("""
1) Adicionar um livro novo ao sistema.
2) Remover um livro da biblioteca.
3) Emprestar um livro.
4) Devolver um livro.
5) Obter relação de todos os livros da biblioteca.
6) Buscar informações sobre um livro específico.
7) Mostrar todos os livros da biblioteca de um determinado autor.
8) Mostrar todos os livros da biblioteca de um determinado gênero.
9) Mostrar relação de todos os livros que estão emprestados.
10) Avaliar um livro (1 a 5 estrelas).
11) Obter a média das avaliações de um livro.
""")

    funcao_digitada = input("Selecione a opção de acordo com o Menu. Para encerrar, digite 0: ")

    match funcao_digitada:
        case "1":  # Guilherme

            # Adicionando o livro e seus dados à biblioteca
            id = int(input("Digite o ID do livro: "))

            if id in biblioteca.keys():
                input("Não é possível adicionar um livro com um ID que já existe. Aperte enter para retornar ao Menu.")
                continue

            titulo = input("Digite o TITULO do livro: ").capitalize()
            autor = input("Digite o AUTOR do livro: ").capitalize()
            ano = int(input("Digite o ANO do livro: "))
            genero = input("Digite o GENERO do livro: ").capitalize()
            adicionar_livro(id, titulo, autor, ano, genero)

        case "2":  # Guilherme

            # Removendo o livro da biblioteca
            id = int(input("Digite o ID do livro a ser removido: "))
            remover_livro(id)

        case "3":  # Gabriel
            id = int(input("Digite a ID do livro a ser emprestado:"))
            if id not in biblioteca.keys():  # Verificar se a ID do livro existe
                input(f"Não foi encontrado o livro de ID {id}! Consulte a lista de livros"
                      f" utilizando a opção de Consultar do índice!")
                continue
            if biblioteca[id]["status"] == "Emprestado":  # Verificar se o livro já está emprestado
                input(f"Infelizmente o livro de ID {id} já está emprestado! Mas vocês ainda pode consultar"
                      f" livros do mesmo gênero ou autor buscando pelas opções disponíveis no índice.")
                continue

            emprestar_livro(id)

        case "4":  # Gabriel

            id = int(input("Digite a ID do livro a ser devolvido:"))
            if id not in biblioteca.keys():  # Verificar se a ID do livro existe
                input(f"Não foi encontrado o livro de ID {id}! Consulte a lista de livros utilizando "
                      f"a opção buscando pelas opções disponíveis no índice.")
                continue
            if biblioteca[id]["status"] == "Disponível":  # Verificar se o livro está disponível
                input(f"O livro de ID {id} já foi devolvido!")
                continue

            devolver_livro(id)

        case "5":  # Juliana
            listar_livros()
        case "6":  # Juliana
            titulo = input("Digite o titulo do livro: ").upper()
            buscar_livro(titulo)

        case "7":  # Raissa
            nome_autor = input("Digite o nome do autor para buscar por seus livros:").upper()
            livros_por_autor(nome_autor)
            input("\nDigite qualquer tecla para retornar ao Menu.")

        case "8":  # Raissa
            genero = input("Digite o gênero de livro que deseja buscar: ").upper()
            livros_por_genero(genero)
            input("\nDigite qualquer tecla para retornar ao Menu.")

        case "9":  # Luis
            livros_emprestado()
            input("\nDigite qualquer tecla para retornar ao Menu.")

        case "10":  # Luis
            x = int(input("Digite o ID do livro: "))
            avaliar_livro(x)
        case "11":  # Luis
            y = int(input("Digite o ID do livro: "))
            obter_media_avaliacoes(y)
        case "0":
            break
        case _:
            input("Entrada inválida! Aperte qualquer tecla para retornar ao Menu.")
            continue
