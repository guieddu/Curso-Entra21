from personagens import Personagem

class Guerreiro(Personagem):
    """Guerreiro representa personagem da classe Mago no jogo.
    
    Attributes:
        nome (str): Nome do Guerreiro.
        nivel (int): Nível do Guerreiro.
        vida (int): Vida do Guerreiro.
        forca (int): Quantidade de força do Guerreiro.
    """

    def __init__(self, nome: str, nivel: int, vida: int, forca: int):
        # Personagem.__init__(nome, nivel, vida)
        super().__init__(nome, nivel, vida)
        self.forca = forca # Atributos específico do Guerreiro

    def atacar(self):
        """Realiza a ação de ataque do mago."""
        super().atacar()
        print(f"{self.nome} desfere um golpe com {self.forca} de forca!")

    def equipar_escudo(self):
        """Realiza a ação de equipar o escudo do Guerreiro."""
        print(f"`{self.nome} equipe o seu escudo! A vida de {self.nome} aumentou.")
        
if __name__ == "__main__":
    Guerreiro = Guerreiro("Guilherme the Warrior", 1, 50, 10)

    Guerreiro.atacar
    Guerreiro.equipar_escudo

