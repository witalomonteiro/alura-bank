class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print(f"Construindo objeto... {self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    # Getters and Setters
    @property
    def numero(self):
        return self.numero

    @property
    def titular(self):
        return self.titular

    @property
    def saldo(self):
        return self.saldo

    @property
    def limite(self):
        return self.limite

    @limite.setter
    def limite(self, valor):
        self.limite = valor

    def imprimir_extrato(self):
         print(f"Titular: {self.__titular}")
         print(f"Saldo: {self.__saldo}")
         print(f"Limite: {self.__limite}\n")

    def __verificar_saque(self, valor):
        valor_disponivel = self.__saldo + self.__limite
        if valor <= valor_disponivel:
            return True
        else:
            return False

    def sacar(self, valor):
        if(self.__verificar_saque(valor)):
            self.__saldo -= valor
            print(f"Realizado saque de {valor} com sucesso!\n")
        else:
            print(f"Saque não realizado! Limite indisponivel!\n")

    def depositar(self, valor):
        self.__saldo += valor
        print(f"Realizado deposito de {valor} com sucesso!\n")

    def transferir(self, conta, valor):
        if (self.__verificar_saque(valor)):
            self.sacar(valor)
            conta.__saldo += valor
            print(f"Realizado transferencia de {valor} para {conta.__titular} com sucesso!\n")
        else:
            print(f"Transferencia não realizada! Limite indisponivel!\n")

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}