import json

from class206_a import SAVE_TO, Test, make_dump

with open(SAVE_TO, 'r') as file:
    data = json.load(file)
    p1 = Test(**data[0])
    p2 = Test(**data[1])
    p3 = Test(**data[2])
    p4 = Test(**data[3])

    print(p1.nome, p1.idade)
    print(p2.nome, p2.idade)
    print(p3.nome, p3.idade)
    print(p4.nome, p4.idade)

    if __name__ == '__main__':
        print('B', __name__)
        make_dump()