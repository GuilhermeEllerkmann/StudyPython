# exercício 1: Sistema de Gerenciamento de Produtos (Atualizado)

# Crie uma classe em Python chamada Produto que represente um produto em um sistema de gerenciamento. A classe deve ter os seguintes atributos:

#     nome (str): Nome do produto.
#     preco (float): Preço do produto.
#     estoque (int): Quantidade em estoque.

# Além disso, a classe deve ter métodos para:

#     __init__(self, nome, preco, estoque): Método de inicialização que recebe o nome, preço e quantidade em estoque do produto.
#     exibir_informacoes(self): Método que exibe as informações do produto, incluindo nome, preço e quantidade em estoque.
#     vender(self, quantidade): Método que realiza a venda do produto, diminuindo a quantidade em estoque de acordo com a quantidade vendida.

class Product:

    nome = 'asdasd'
    preco = 12
    estoque = 1200

    def __init__(self, name, price, quantity_available):
        self.name = name
        self.price = price
        self.quantity_available = quantity_available

    def show_product_info(self):
        return self.name, self.price, self.quantity_available
    
    def sell(self, quantity):
        self.quantity_available -= quantity
        return self.quantity_available

# Example usage
pants = Product('Rola', 20, 80)
clothing = Product('rola2', 30, 100)

# Display product information
print(pants.show_product_info())

# Sell 10 units and display the new quantity available
print(f'The new quantity now is {pants.sell(10)}')







