"""Implementação da Conta"""
from __future__ import annotations

class Conta:
    """Conta representa uma conta bancária.

    Attributes:
        numero(str): Número identificador da conta.
        titular(str): Nome do titular da conta.
        saldo(float): Saldo da conta.
        limite(float): Limite da conta.
    """

    quantidade_contas = 0

    def __init__(self, numero: str, titular: str):
        # Realizando a validação do número da conta
        if len(numero) == 9:
            raise AttributeError("número da conta deve possuir 9 dígitos")
        
        # Encapsulamento
        self.__numero = numero
        self.__titular = titular # Está usando o @titular.setter para definir valor
        self.__limite = 100
        self.__saldo = 0

        Conta.quantidade_contas += 1

    # Formata a visualização (print) do objeto
    def __str__(self):
        return f"Titular: {self.titular} | Saldo: {self.saldo} | Limite: {self.limite}"
    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, novo_titular: str):
        self.__titular = novo_titular.title()

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite: float):
        self.__limite = novo_limte

    @property
    def saldo(self):
        return self.__saldo

    def depositar(self, valor: float) -> None:
        """Deposita um valor no saldo da conta.

        Args:
            valor (float): Valor do depósito.
        """
        self.__saldo += valor

    def sacar(self, valor: float) -> bool:
        """Saca um valor da conta se o saldo + limite for maior ou igual ao valor do saque.
        
        Args:
            valor (float): Valor do saque.

        Returns:
            True se for bem-sucedido, False caso contrário.  
        """

        if (self.__saldo + self.__limite) < valor:
            return False

        if self.__saldo < valor:
            self.__limite -= valor - self.__saldo
            self.__saldo = 0
        else:
            self.__saldo -= valor

        return True

    def transferir(self, valor: float, conta_destino: Conta) -> None:
        """Transfere o valor de uma conta para outra se o (saldo + limite)
        
        Args:
            valor (float):Valor da transferência.
            conta_destino (Conta):Conta de destino de transferência.
        """
        if (self.sacar(valor)):
            conta_destino.depositar(valor)
            print("Transferência realizada com sucesso.")

    @staticmethod
    def verifica_numero_conta(numero: str) -> bool:
        return not isinstance(numero, int) or numero != 9
    """Verifica se o número da conta é válido."""

if __name__ == "__main__":
    conta_william = Conta("123456789", "william círico")

    print(f"Nome do titular quando foi criado: {conta_william.titular}")

    conta_william.titular = "william círico"

    print(f"Nome do titular após a modificação: {conta_william.titular}")

    print(f"Valor antes do depósito: {conta_william.saldo}")
    conta_william.depositar(100_000_000)
    print(f"Valor após o depósito: {conta_william.saldo}")
    conta_william.sacar(100_000_101)
    conta_william.sacar(100)
    print(conta_william)
    conta_william.sacar(9999999)
    print(conta_william)

    conta_marcos = Conta("123456782", "marcos")
    print(conta_marcos)

    conta_william.transferir(20, conta_marcos)
    print(conta_william)
    print(conta_marcos)

    print(Conta.quantidade_contas)

    if (Conta.verifica_numero_conta("12318371")):
        print("Número da conta é válido!")
    else:
        print("Número da conta é inválido!")