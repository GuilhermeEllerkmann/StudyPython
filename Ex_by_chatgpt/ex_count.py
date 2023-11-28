# Exercício: Contagem de Elementos Únicos
# Escreva uma função chamada unique_elements_counter que recebe uma lista como parâmetro e retorna um dicionário contendo a contagem de elementos únicos na lista.

from itertools import count

def unique_elements_counter(param):
    dic = {}
    for i in param :
        count_numbers = param.count(i)
        dic[f'Number {i}'] = count_numbers
    return dic

example_list = [1, 2, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9]
output = unique_elements_counter(example_list)
print(output)
