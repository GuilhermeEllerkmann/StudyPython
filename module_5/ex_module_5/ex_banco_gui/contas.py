from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, numero_conta, saldo):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor):...

    def depositar(self, valor):
        if valor >= 0:
            self.saldo += valor
        print(f'Depositado o valor de R${valor:.2f}, seu saldo total agora eh de R${self.saldo:.2f}')

class ContaCorrente(Conta):
    def __init__(self, agencia, numero_conta, saldo, limite_extra):
        super().__init__(agencia, numero_conta, saldo)
        self.limite_extra = limite_extra
        self.id_user = None

    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite_extra

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            print(f'Saque de R${valor} realizado, seu saldo agora eh de {self.saldo}')
            return self.saldo

        print('Não foi possível sacar o valor desejado')
        print(f'Seu limite é {-self.limite_extra:.2f}')

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.numero_conta!r}, {self.saldo!r}, {self.limite_extra!r}, {self.id_user!r})'
        return f'{class_name}{attrs}'

class ContaPoupanca(Conta):
    def __init__(self, agencia, numero_conta, saldo,):
        super().__init__(agencia, numero_conta, saldo)
        self.id_user = None

    def sacar(self, valor):
        if valor > self.saldo:
            print(f'Seu saldo eh de {self.saldo}, portanto nao sera possivel sacar o valor desejado de {valor}')

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.numero_conta!r}, {self.saldo!r}, {self.id_user!r})'
        return f'{class_name}{attrs}'