# Exercício 1: Sistema de Formas Geométricas
# Descrição: Crie uma classe abstrata chamada FormaGeometrica usando o módulo abc. 
# Esta classe deve ter um método abstrato chamado area e um método abstrato chamado perimetro. 
# Implemente classes derivadas como Circulo, Retangulo e Triangulo, fornecendo implementações para os métodos area e perimetro.
from abc import ABC, abstractmethod
PI = 3.14

class FormaGeometrica(ABC):
    
    @abstractmethod
    def area(self):
        ...

    @abstractmethod
    def perimetro(self):
        ...

    def area_perimetro(self):
        print('calculando area e perimetro')
        print(self.area())
        print(self.perimetro())

class Retangulo(FormaGeometrica):
    
    def __init__(self, altura, largura):
        self._altura = altura
        self._largura = largura

    def area(self):
        return self._altura * self._largura
    
    def perimetro(self):
        return (self._altura * 2) + (self._largura * 2)
    
    def area_perimetro(self):
        print('calculando area e perimetro')
        print(self.area())
        print(self.perimetro())
    
class Circulo(FormaGeometrica):

    def __init__(self, raio):
        self._raio = raio

    def area(self):
        return PI * (self._raio * self._raio)     

    def perimetro(self):
        return 2 * PI * self._raio
    
class Triangulo(FormaGeometrica):

    def __init__(self, raio):
        self._raio = raio
        
    def perimetro(self):
        return 2 * PI * self._raio
    
    def area(self):
        return PI * (self._raio * self._raio)

ret = Retangulo(5, 10)
ret.area_perimetro()


circ = Circulo(5)
circ.area_perimetro()

triang = Triangulo(12.5)
triang.area_perimetro()