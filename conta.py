
class Conta:
    # função com OO pelos dois underscores, para privar e chamar pelo self.
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    # property acessando como se fosse atributo
    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self): # get devolve
        return self.__limite

    @limite.setter
    def limite(self, limite): # set envia
        self.__limite = limite

    # modo statico podemos chamar ele sem criar a conta.
    @staticmethod
    def codigos_banco():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}