# Exercício 2: Calculadora Avançada

# Desenvolva uma classe em Python chamada CalculadoraAvancada que implementa funções avançadas de uma calculadora. A classe deve ter os seguintes métodos:

#     soma(self, *numeros): Retorna a soma dos números fornecidos como argumentos.
#     subtracao(self, a, b): Retorna a subtração de a por b.
#     multiplicacao(self, *numeros): Retorna o produto dos números fornecidos como argumentos.
#     divisao(self, a, b): Retorna a divisão de a por b.
#     potencia(self, base, expoente): Retorna a potência de base elevada a expoente.
#     raiz_quadrada(self, numero): Retorna a raiz quadrada do número fornecido.
import math

class AdvancedCalc():

    def __init__(self) -> None:
        pass

    def addition(self, a, b):
        return a + b
        
    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        return a / b

    def exponentiation(self, numbase, exponent):
        return numbase ** exponent

    def square_root(self, num):
        return round(math.sqrt(num), 2)
    
calc = AdvancedCalc()

print(calc.addition(10,20))
print(calc.subtraction(30, 10))
print(calc.multiplication(10, 5))
print(calc.division(10, 2))
print(calc.exponentiation(2, 2))
print(calc.square_root(5))