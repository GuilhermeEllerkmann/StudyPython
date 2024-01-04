# Exercício 2: Processamento de Arquivos
# Descrição: Desenvolva uma classe abstrata ProcessadorDeArquivo com um método abstrato processar. Esta classe será a base para processar diferentes tipos de arquivos. 
# Crie classes derivadas como ProcessadorCSV, ProcessadorTXT e ProcessadorJSON, implementando o método processar para lidar com a leitura e o processamento específico de cada tipo de arquivo.
from abc import ABC, abstractmethod

class ProcessadorDeArquivo(ABC):

    @abstractmethod
    def processar(self, nome_arquivo):
        ...

    def show_info(self):
        print(self.processar())


class ProcessadorCSV(ProcessadorDeArquivo):

    def __init__(self, nome_arquivo):
        self._nome_arquivo = nome_arquivo

    def processar(self):
        return f'o nome do arquivo eh {self._nome_arquivo} e eh do tipo CSV'

class ProcessadorTXT(ProcessadorDeArquivo):

    def __init__(self, nome_arquivo):
        self._nome_arquivo = nome_arquivo

    def processar(self):
        return f'o nome do arquivo eh {self._nome_arquivo} e eh do tipo TXT'
    
class ProcessadorJSON(ProcessadorDeArquivo):

    def __init__(self, nome_arquivo):
        self._nome_arquivo = nome_arquivo

    def processar(self):
        return f'o nome do arquivo eh {self._nome_arquivo} e eh do tipo JSON'
    
arc_CSV = ProcessadorCSV('arquivo 1')
arc_TXT = ProcessadorTXT('arquivo 2')
arc_JSON = ProcessadorJSON('arquivo 3')

arc_CSV.show_info()
arc_TXT.show_info()
arc_JSON.show_info()
