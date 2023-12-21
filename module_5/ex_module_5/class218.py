# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro():
    def __init__(self, nome_carro):
        self.carro = nome_carro
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, nome_motor):
        self._motor = nome_motor

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante
        

class Motor():
    def __init__(self, nome):
        self.motor = nome

    def list_motor(self):
        return f' o motor eh {self.motor}'
        

class Fabricante():
    def __init__(self, fabricante):
        self.fabricante = fabricante

    def list_fabricante(self):
        return f' o fabricante eh {self.fabricante}'
        
corsa = Carro('Corsa')
fabricante = Fabricante('GM')
motor = Motor('1.8 flex')
corsa.motor = motor
corsa.fabricante = fabricante

print(corsa.motor.list_motor())
print(corsa.fabricante.list_fabricante())