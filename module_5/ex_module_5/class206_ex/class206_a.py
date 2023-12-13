# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json
import os
SAVE_TO = '/home/gui/Desktop/Curso_python/module_5/ex_module_5/class206_ex/jason_class206.json'

class Test:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

person_1 = Test('John', '25')
person_2 = Test('Ashley', '15')
person_3 = Test('William', '23')
person_4 = Test('Jonas', '44')

persons_list = [vars(person_1), vars(person_2), vars(person_3), vars(person_4)]


def make_dump():
    with open(SAVE_TO, 'w') as file:
        json.dump(persons_list, file, indent=2)


if __name__ == '__main__':
    print('A', __name__)
    make_dump()