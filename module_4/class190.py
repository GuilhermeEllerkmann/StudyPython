'/home/gui/Desktop/Curso_python/GitHub/module_4/json_package/aula190.json'

import json

# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'enderecos': [
#         {'rua': 'R1', 'numero': 32},
#         {'rua': 'R2', 'numero': 55},
#     ],
#     'altura': 1.8,
#     'numeros_preferidos': (2, 4, 6, 8, 10),
#     'dev': True,
#     'nada': None,
# }

# with open('/home/gui/Desktop/Curso_python/GitHub/module_4/json_package/aula190.json', 'w') as arquivo:
#     json.dump(pessoa, arquivo, indent=2)

with open('/home/gui/Desktop/Curso_python/GitHub/module_4/json_package/aula190.json', 'r') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa['nome'])