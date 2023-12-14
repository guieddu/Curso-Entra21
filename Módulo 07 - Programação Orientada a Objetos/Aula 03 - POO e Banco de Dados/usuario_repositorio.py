from typing import Any, List
import sqlite3
from usuario import Usuario

class UsuarioRepositorio:
    """Repositório de usuários."""
    def __init__(self, db_nome: str) -> None:
        self.db_nome = db_nome

    # CUD
    # CREATE
    # READ
    # UPDATE
    # DELETE

    def __executar_query(self, query: str, *params: Any) -> None:
        """Executa uma query no banco de dados.
        
        Args:
            query (str): Query que será executada.
            params (Any): Parâmetros da query.
        """
        connection = sqlite3.connect(self.db_nome) # Abriu uma conexão com sqlite
        cursor = connection.cursor() 
        cursor.execute(query, params) # Executar a query
        connection.commit() # Comitar as alterações feitas pela consulta
        connection.close() # Fecha a conexão com o banco de dados

    def inserir_usuario(self, usuario: Usuario) -> Usuario:
        """Insere um usuário no banco de dados. O objeto usuário é atualizado com o ID do banco.
        
        Args:
            usuario (Usuario): Usuário que será criado.
        """
        query = "INSERT INTO usuarios (nome_usuario, email) VALUES (?, ?)"
        self.__executar_query(query, usuario.nome_usuario, usuario.email)

        usuario_id = self.get_ultimo_id_inserido()
        print(usuario_id)
        usuario.id = usuario_id

        return usuario

    def atualizar_usuario(self, usuario: Usuario) -> None:
        """Atualiza os dados de um usuário no banco de dados."""
        query = "UPDATE usuarios SET nome_usuario = ?, email = ? WHERE id = ?"
        self.executar_query(query, usuario.nome_usuario, usuario.email, usuario.id)

    def remover_usuario(self, usuario: Usuario) -> None:
        """Remove um usuário do banco de dados."""
        query = "DELETE FROM usuarios WHERE id = ?"
        self.executar_query(query, usuario.id)

    def obter_usuarios(self) -> List[Usuario]:
        """Obtém todos os usuários cadastrados no banco de dados."""
        query = "SELECT * FROM usuarios;"
        connection = sqlite3.connect(self.db_nome)
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        connection.close()
        # (1, "William", "william@email.com")
        return [Usuario(row[1], row[2], row[0]) for row in rows]
    
    def get_ultimo_id_inserido(self) -> int:
        """Retorna o ID do último registro inserido no banco de dados."""
        query = "SELECT id FROM usuarios ORDER BY 1 DESC LIMIT 1;"
        connection = sqlite3.connect(self.db_nome)
        cursor = connection.cursor()
        cursor.execute(query)
        row = cursor.fetchone()
        connection.close()
        return row[0]