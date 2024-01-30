class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Cliente(Pessoa):
    def __init__(self, id, nome, idade):
        super().__init__(nome, idade)
        self.id = id
        self.conta = None

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.id!r}, {self.nome!r}, {self.idade!r}, {self.conta!r})'
        return f'{class_name}{attrs}'