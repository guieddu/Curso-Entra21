from 

class Combate:
    """Combate representa uma partidad o jogo.
    
    Attributes:
        personagem1 (Personagem): Personagem 1.
        personagem2 (Personagem): Personagem 2.
    """

    def __init__(self, personagem1: Personagem, personagem2: Personagem):
        if not isinstance(personagem1, Personagem):
            raise TypeError("personagem 1 precisa ser do tipo Personagem")
        
        if not isinstance(personagem2, Personagem):
            raise TypeError("personagem 2 precisa ser do tipo Personagem")

            self.personagem1 = personagem1
            self.personagem2 = personagem2


    def iniciar_combate(self):
        """Incia o combate entre dois personagens."""
        print(f"Início do combate entre {self.personagem1.nome} e {self.personagem2.nome}")

        self.personagem1.atacar()
        self.personagem2.defender()

        self.personagem2.atacar()
        self.personagem1.defender()

        self.personagem1.atacar()
        self.personagem2.morrer()

        print("Fim do combate")

if __name__ == "__main__":
    will_mage = Mago("William the Mage", 1, 10, 10)
    guilherme_warrior = Guerreiro("Guilherme the Warrior", 1, 50, 10)

    combate = Combate(will_mage, guilherme_warrior)
    combate.iniciar.combate()






