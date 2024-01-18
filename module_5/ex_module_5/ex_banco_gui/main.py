"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clientes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método (autenticar).
"""
import pessoas, contas, os, time, emoji
from banco import Bancos

class Conta():
    def __init__(self, nome = None, idade = None, tipo_de_conta = None, login = None, senha = None) -> None:
        self.nome = nome
        self.idade = idade
        self.tipo_de_conta = tipo_de_conta
        self.login = login
        self.senha = senha

class Commands:
    def __init__(self) -> None:
        pass

    def exibir_boas_vindas():
        print("Bem-vindo ao Banco Python!")
        print("------------------------------")
        print("Escolha uma opção:")
        print("1. Ver saldo")
        print("2. Realizar depósito")
        print("3. Realizar saque")
        print("4. Sair")

def main():
    print('Bem vindo ao banco Dos-Corno')
    print('-------------||-------------')
    Conta.nome = input('Digite seu nome: ').upper().strip()
    Conta.idade = input('Digite sua idade: ').upper().strip()
    Conta.tipo_de_conta = input('Digite C para conta corrente e P para conta poupanca: ').upper().strip()
    Conta.login = input('Digite seu login: ').strip()
    Conta.senha = input('Digite seu senha: ').strip()
    print('Ok, conta criada, seus dados sao: ', (Conta.nome, Conta.idade, Conta.tipo_de_conta, Conta.login, Conta.senha))
    print(f'Carregando pagina de login {emoji.emojize(":octopus:")}')
    time.sleep(5)
    print('-------------||-------------')

    os.system('clear')
    Commands.exibir_boas_vindas()





if __name__ == '__main__':
    main()
