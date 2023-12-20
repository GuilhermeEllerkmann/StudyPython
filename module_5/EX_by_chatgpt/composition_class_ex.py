# Exercício sobre Agregação em Python

# Imagine um sistema de gerenciamento de biblioteca. Crie três classes: Livro, Autor, e Biblioteca.

#     Livro: Representa um livro com atributos como título, ISBN, e ano de publicação.

#     Autor: Representa um autor com atributos como nome e nacionalidade. Um autor pode ter escrito vários livros.

#     Biblioteca: Representa uma biblioteca que contém uma coleção de livros. Cada livro na biblioteca está associado a um autor.

# Tarefas:

#     Crie instâncias de autores e livros, associando livros a autores.
#     Adicione livros à biblioteca, garantindo a agregação entre a biblioteca e os livros.
#     Exiba a lista de livros na biblioteca com detalhes, incluindo o nome do autor de cada livro.

# Este exercício ajudará a entender como as classes podem estar associadas de forma agregada, onde uma classe contém uma coleção de instâncias de outra classe, mas ambas podem existir independentemente.
#testing ssh
#testing sasdasd

class Author():

    def __init__(self, name, born):
        self.name = name
        self.born = born

    def escrever(self):
        return f'o autor eh {self.name} e ele nasceu em {self.born}'

class Book():

    def __init__(self, title, isbn, data_published):
        self.title = title
        self.isbn = isbn
        self.data_published = data_published
        self._author = None

    def escrever_dados_livro(self):
        return f'O Nome do livro eh {self.title}, tem nota de {self.isbn}, e foi publicado em {self.data_published}'

    @property
    def autor(self):
        return self._author
    
    @autor.setter
    def autor(self, autor):
        self._author = autor

class Library():

    def __init__(self):
        self.__books = None
        self.__collection = []

    @property
    def livro(self):
        return self.__books
    
    @property
    def colection(self):
        for item in self.__collection:
            i = (item.title, item.autor.name)
        
        return i
    
    @livro.setter
    def livro(self, livro):
        self.__books = livro

    def add_collection(self, livro):
        self.__collection.append(livro)


livraria = Library() # Init da livraria


#livro 1 dados

autor1 = Author('Gui', '22/07')
livro1 = Book('ROSA DE SARON', '123', '11/02')
livro1.autor = autor1
livraria.livro = livro1
livraria.add_collection(livro1)

#livro 2 dados
autor2 = Author('Giovana', '16/10')
livro2 = Book('Linda de bonita', '234', '11/05')
livro2.autor = autor2
livraria.livro = livro2
livraria.add_collection(livro2)

print(livraria.colection)
