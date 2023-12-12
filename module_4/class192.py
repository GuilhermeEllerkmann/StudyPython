# Problema dos parâmetros mutáveis em funções Python
def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


lista_de_doces = adiciona_clientes('doce de abobora')
adiciona_clientes('rapadura', lista_de_doces)
adiciona_clientes('maria mole', lista_de_doces)
adiciona_clientes('teta de nega', lista_de_doces)

lista_de_carros = adiciona_clientes('Toyota')
adiciona_clientes('GM', lista_de_carros)
adiciona_clientes('Honda', lista_de_carros)
adiciona_clientes('Wolk', lista_de_carros)


print(lista_de_doces)
print(lista_de_carros)