# Crie um programa em Python que utilize uma função recursiva para calcular o fatorial de um número. 
# O programa deve receber um número como entrada e imprimir o fatorial correspondente.

def factorial(n):
    if n <=1:
        return 1
    
    return n * factorial(n - 1)

print(factorial(5))