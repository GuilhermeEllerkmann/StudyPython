# Exercício 1: Sistema de Formas Geométricas
# Descrição: Crie uma classe abstrata chamada FormaGeometrica usando o módulo abc. 
# Esta classe deve ter um método abstrato chamado area e um método abstrato chamado perimetro. 
# Implemente classes derivadas como Circulo, Retangulo e Triangulo, fornecendo implementações para os métodos area e perimetro.
from abc import ABC, abstractmethod
PI = 3.141592

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
    
# class Triangulo(FormaGeometrica):

#     def __init__(self, a, b, c):
#         self._a = a
#         self._b = b
#         self._c = c

#     def is_triangle(self):

#         if self._a + self._b > self._c and self._a + self._c > self._b and self._b + self._self._a > self._c and self._b + self._c > self._a and self._c + self._a > self._b and self._c + self._b > self._a:
#             return True
#         else:
#             return False
        
#     def area(self):
        
    
    


ret = Retangulo(5, 10)
ret.area_perimetro()


circ = Circulo(5)
circ.area_perimetro()