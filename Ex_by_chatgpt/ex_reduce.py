# Crie um programa em Python que utilize a função reduce do módulo functools 
# para calcular o produto de uma lista de números. 
# O programa deve receber uma lista de números como entrada e 
# imprimir o produto acumulado.

from functools import reduce

list_of_numbers = [10,20,30,40,50]


total = reduce(
  lambda ac, x: ac + x,
  list_of_numbers,
  0
)

print('the total amount is:',total)