# Crie um programa em Python que utilize a função partial da biblioteca functools para criar uma versão parcial de uma função de soma, fixando um dos operandos. 
# Em seguida, use a função parcial para criar uma função que soma 10 a qualquer número dado como entrada.
from functools import partial

def regular_sum(a, b):
    return a + b

def par():
    ad_with_10 = partial(regular_sum, 10)

    number_by_user = int(input(f'Type one number to ad to 10:'))

    result = ad_with_10(number_by_user)

    return print(f'{number_by_user} plus 10 is {result}')

par()
