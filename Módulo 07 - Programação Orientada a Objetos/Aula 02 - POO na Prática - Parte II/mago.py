from personagens import Personagem
from habilidade_especial import IHabilidadeEspecial

class Mago(Personagem, IHabilidadeEspecial):
    """Mago representa personagem da classe Mago no jogo.
    
    Attributes:
        nome (str): Nome do mago.
        nivel (int): Nível do mago.
        vida (int): Vida do mago
        magia (int): Quantidade de magia do mago.
    """

    def __init__(self, nome: str, nivel: int, vida: int, magia: int):
        # Personagem.__init__(nome, nivel, vida)
        super().__init__(nome, nivel, vida)
        self.magia = magia # Atributos específico do mago

    def atacar(self):
        """Realiza a ação de ataque do mago."""
        super().atacar()
        print(f"{self.nome} lança um feitiço poderoso com {self.magia} de magia!")

    def equipar_cajado(self):
        """Realiza a ação de equipar o cajado do mago."""
        print(f"`{self.nome} equipe o seu cajado! O próximo ataque causará dano em área.")

    def usar_super_habilidade(self):
        """Utilizar a super habilidade do mago."""
        print(f"{self.nome} utiliza a super habilidade especial Meteoro! Todos os inimigos perdem 99% de sua vida.")
        
if __name__ == "__main__":
    mago = Mago("Guilherme the Mage", 1, 10, 11)

    print(mago.nome)
    print(mago.magia)

    mago.atacar()

