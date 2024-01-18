import enum

# Defina a enumeração Cores aqui
class Cores(enum.Enum):
    VERMELHO = enum.auto()
    VERDE = enum.auto()
    AZUL = enum.auto()
    AMARELO = enum.auto()

# Implemente a função mostrar_cor
def mostrar_cor(cor: Cores):
    if not isinstance(cor, Cores):
        raise ValueError('Encontrei essa porra n')
    
    print(f'A cor eh {cor.name} e o valor eh {cor.value}')


# Teste a função com diferentes cores
mostrar_cor(Cores.AMARELO)