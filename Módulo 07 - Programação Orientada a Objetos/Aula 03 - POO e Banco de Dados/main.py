from inicializador_bd import InicializadorBD
from usuario_repositorio import UsuarioRepositorio
from usuario import Usuario

DB_NOME = "exemplo.sqlite"
InicializadorBD.criar_tabelas(DB_NOME)

usuario_repositorio = UsuarioRepositorio(DB_NOME)

usuario1 = Usuario("William Círico", "contato.williamc@gmail.com")

usuario_repositorio.inserir_usuario(usuario1)

print(usuarios)