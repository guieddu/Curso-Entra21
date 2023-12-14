class Imovel:
    def __init__(self, endereco, preco):
        self.endereco = endereco
        self.preco = preco

    def get_endereco(self):
        return self.endereco

    def get_preco(self):
        return self.preco

    def imprimir_informacoes(self):
        print(f"Endereço: {self.endereco}\nPreço: R${self.preco:.2f}")


class Novo(Imovel):
    def __init__(self, endereco, preco, adicional):
        super().__init__(endereco, preco)
        self.adicional = adicional

    def get_adicional(self):
        return self.adicional

    def set_adicional(self, adicional):
        self.adicional = adicional

    def imprimir_informacoes(self):
        preco_final = self.preco + self.adicional
        print(f"Endereço: {self.endereco}\nPreço Base: R${self.preco:.2f}\nAdicional: R${self.adicional:.2f}\nPreço Final: R${preco_final:.2f}")


class Velho(Imovel):
    def __init__(self, endereco, preco, desconto):
        super().__init__(endereco, preco)
        self.desconto = desconto

    def get_desconto(self):
        return self.desconto

    def set_desconto(self, desconto):
        self.desconto = desconto

    def imprimir_informacoes(self):
        preco_final = self.preco - self.desconto
        print(f"Endereço: {self.endereco}\nPreço Base: R${self.preco:.2f}\nDesconto: R${self.desconto:.2f}\nPreço Final: R${preco_final:.2f}")


imovel1 = Imovel("Rua A, 123", 200000)
imovel1.imprimir_informacoes()

novo1 = Novo("Rua B, 456", 250000, 30000)
novo1.imprimir_informacoes()

velho1 = Velho("Rua C, 789", 180000, 20000)
velho1.imprimir_informacoes()
