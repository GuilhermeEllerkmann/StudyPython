from itertools import product

# Exercício: Um fabricante de carros oferece um modelo de carro com 4 opções de cores e 3 opções de acabamento interior. 
# Além disso, o cliente pode escolher entre 2 tipos de rodas. 
# Quantas diferentes combinações de carro o cliente pode criar escolhendo uma cor, um acabamento e um tipo de roda?

data_car = [
    ['blue', 'black', 'orange', 'red'],
    ['acab1', 'acab2', 'acab3'],
    ['wheels1', 'wheels2'],
]

print(f'Tem um total de {len(list(product(*data_car)))} de combinacoes')
