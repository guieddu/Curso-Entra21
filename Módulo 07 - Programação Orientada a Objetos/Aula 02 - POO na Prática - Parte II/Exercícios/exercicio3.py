class Conta:
    def __init__(self, numero_conta, titular, saldo):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        taxa = self.get_taxa_deposito()
        valor_deposito = valor - (valor * taxa)
        self.saldo += valor_deposito
        return f"Depósito de {valor} realizado. Saldo atual: {self.saldo}"

    def sacar(self, valor):
        if valor > self.saldo:
            return "Saldo insuficiente."
        self.saldo -= valor
        return f"Saque de {valor} realizado. Saldo atual: {self.saldo}"

    def transferir(self, conta_destino, valor):
        if valor > self.saldo:
            return "Saldo insuficiente para transferência."
        self.saldo -= valor
        conta_destino.saldo += valor
        return f"Transferência de {valor} para a conta {conta_destino.numero_conta} realizada. Saldo atual: {self.saldo}"

    def get_taxa_deposito(self):
        return 0.0

class ContaCorrente(Conta):
    def __init__(self, numero_conta, titular, saldo, limite):
        super().__init__(numero_conta, titular, saldo)
        self.limite = limite

    def sacar(self, valor):
        if valor > (self.saldo + self.limite):
            return "Limite de saque ultrapassado."
        self.saldo -= valor
        return f"Saque de {valor} realizado. Saldo atual: {self.saldo}"

    def transferir(self, conta_destino, valor):
        if valor > (self.saldo + self.limite):
            return "Limite de transferência ultrapassado."
        self.saldo -= valor
        conta_destino.saldo += valor
        return f"Transferência de {valor} para a conta {conta_destino.numero_conta} realizada. Saldo atual: {self.saldo}"

    def get_taxa_deposito(self):
        return 0.002

class ContaPoupanca(Conta):
    def calcular_juros(self):
        juros = self.saldo * 0.005
        self.saldo += juros
        return f"Juros de {juros} aplicados. Saldo atual: {self.saldo}"

    def get_taxa_deposito(self):
        return 0.005

class ContaInvestimento(Conta):
    def investir_acoes(self, valor):
        return f"Investimento em ações no valor de {valor} realizado. Saldo atual: {self.saldo}"

    def get_taxa_deposito(self):
        return 0.008

conta_corrente = ContaCorrente(numero_conta="123", titular="João", saldo=1000, limite=500)
conta_poupanca = ContaPoupanca(numero_conta="456", titular="Maria", saldo=2000)
conta_investimento = ContaInvestimento(numero_conta="789", titular="Carlos", saldo=3000)

print(conta_corrente.depositar(500))
print(conta_corrente.sacar(1200))

print(conta_poupanca.depositar(1000)) 
print(conta_poupanca.calcular_juros())

print(conta_investimento.depositar(2000))
print(conta_investimento.investir_acoes(1000))
