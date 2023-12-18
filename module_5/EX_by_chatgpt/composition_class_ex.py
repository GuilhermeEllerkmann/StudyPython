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


class Book():

    def __init__(self, title, isbn, data_published):
        self.title = title
        self.isbn = isbn
        self.data_published = data_published
        self._autor = None

    @property
    def autor(self):
        return self._autor
    
    @autor.setter
    def set_autor(self, autor):
        self._autor = autor




class Author():

    def __init__(self, name, born):
        self.name = name
        self.born = born

    def escrever(self):
        return f'{self.name} eh o escritor'


class Library():

    def __init__(self, books, author):
        self.books = books
        self.author = author


autor = Author('Gui', 'Lins')
livro = Book('a rosa de saron', '123', '22/07')
livro.set_autor = autor

print(livro.autor.escrever())