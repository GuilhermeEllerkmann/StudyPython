import pessoas
import contas
import os
import time
import random
import emoji
import json


DICT_USER_SENHA = '/home/gui/Desktop/Curso_python/module_5/ex_module_5/ex_banco_gui/users.json'
DICT_CONTA = '/home/gui/Desktop/Curso_python/module_5/ex_module_5/ex_banco_gui/contas.json'

class Commands:
    @staticmethod
    def login_ou_criar():
        print('Já é cadastrado? Aperte 1 para logar')
        print('Não é cadastrado? Aperte 2 para criar sua conta')

    @staticmethod
    def exibir_boas_vindas():
        print("Bem-vindo ao banco Dos-Corno")
        print("------------------------------")
        print("Escolha uma opção:")
        print("1. Ver saldo")
        print("2. Realizar depósito")
        print("3. Realizar saque")
        print("4. Sair")

    @staticmethod
    def separador():
        print('-------------||-------------')

    @staticmethod
    def limpa_tela():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    @staticmethod
    def ver_saldo(cliente):
        os.system('clear')
        print(f'R${cliente.saldo:.2F}')
        Commands.esperar(3)
        os.system('clear')

    @staticmethod
    def depositar(cliente):
        os.system('clear')
        valor = int(input('Digite o valor do depósito: '))
        cliente.depositar(valor)
        Commands.esperar(3)
        os.system('clear')

    @staticmethod
    def sacar(cliente):
        os.system('clear')
        valor = int(input('Digite o valor a sacar: '))
        cliente.sacar(valor)
        Commands.esperar(3)
        os.system('clear')

    @staticmethod
    def valida_login(login, senha, contas):
        return True if (login, senha) in contas else False

    @staticmethod
    def realiza_login(login_valido):
        Commands.limpa_tela()
        if login_valido:
            print('Login validado')
        else:
            print('Login inválido, tente novamente')

    @staticmethod
    def esperar(sec=3):
        time.sleep(sec)

    @staticmethod
    def criar_conta(tipo_de_conta, cliente):
        if tipo_de_conta == 'C':
            cliente_conta = contas.ContaCorrente(111, 222, 0, 100)
            cliente.conta = cliente_conta
            return cliente_conta
        else:
            cliente_conta = contas.ContaPoupanca(222, 333, 0)
            cliente.conta = cliente_conta
            print(f'Conta corrente criada, sua agência é {contas.ContaCorrente}')
            return cliente_conta
        
    def read_data(dict):
        with open(dict, 'r') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
            return data
        
    def cria_arquivo_json(diretorio, dic):
        try:
            print('to aqui 1')
            with open(diretorio, 'r') as file:
                
                dados_existentes = json.load(file)

                dados_existentes.append(dic)

                with open(diretorio, 'w') as file:
                    json.dump(dados_existentes, file, indent=2)
        except AttributeError:
            print('to aqui 2')
            with open(diretorio, 'r') as file:
                dados_existentes = json.load(file)

                dados_existentes = [dados_existentes]
                dados_existentes.append(dic)

                with open(diretorio, 'w') as file:
                    json.dump(dados_existentes, file, indent=2)

        except FileNotFoundError:
            print('to aqui 3')
            dados_existentes = []

            dados_existentes.append(dic)

            with open(diretorio, 'w') as file:
                json.dump(dados_existentes, file, indent=2)

        except json.decoder.JSONDecodeError:
            print('to aqui 4')
            print('Vazio ou invalido, adicionando novo conjunto de dados')

            with open(diretorio, 'w') as file:
                json.dump(dic, file, indent=2)
            
            with open(diretorio, 'r') as file:
                dados_existentes = json.load(file)

        
class SetID:

    def __init__(self):
        self.ids_existentes = set()

    def adicionar_id(self, novo_id):
        if novo_id in self.ids_existentes:
            print(f'ID {novo_id} ja existe')
        else:
            self.ids_existentes.add(novo_id)
            print(f'ID {novo_id} adicionado com sucesso')
            return novo_id

    def verificar_existencia(self, id_verificar):
        return id_verificar in self.ids_existentes
        


def main():
    dados_users = Commands.read_data(DICT_USER_SENHA)
    dados_contas = Commands.read_data(DICT_CONTA)

   
    login_ou_criar = input('Logar(L) ou criar conta(C)?').upper().strip()


    if login_ou_criar == 'L':
        login = input('Login: ').upper().strip()
        senha = input('Senha: ').upper().strip()
        for user in dados_users:
            if user["login"] == login and user["senha"] == senha:
                print(f"Login e senha encontrados! ID: {user['id']}")
                id = user['id']
                nome = user['nome']
                idade = user['idade']
                for user_data in dados_contas:
                    if user_data["id_user"] == id:
                        agencia = user_data['agencia']
                        numero_conta = user_data['numero_conta']
                        saldo = user_data['saldo']
                        id_user = user_data['id_user']
                        if numero_conta == 222:
                            cliente = pessoas.Cliente(id_user, nome, idade)
                            conta_cliente = contas.ContaCorrente(agencia,numero_conta,saldo,100)
                            cliente.conta = conta_cliente
                            conta_cliente.id_user = id
                            print(cliente)

                        if numero_conta == 333:
                            cliente = pessoas.Cliente(id_user, nome, idade)
                            conta_cliente = contas.ContaPoupanca(agencia,numero_conta,saldo)
                            cliente.conta = conta_cliente
                            conta_cliente.id_user = id
                            print(cliente)
                break
            else:
                print('Proximo...')


    else:
        gerar_id = SetID()
        id = gerar_id.adicionar_id(random.randint(1000,9999))
        while gerar_id.verificar_existencia(id) == False:
            id = gerar_id.adicionar_id(random.randint(1000,9999))
            print('cheguei aqui')
            print (id)

        login = input('Digite seu login').upper().strip()
        senha = input('Digite sua senha').upper().strip()
        nome_cliente = input('Digite seu nome').upper().strip()
        idade_cliente = input('Digite sua idade').upper().strip()
        dados_login = {
            "id": id,
            "login": login,
            "senha": senha,
            "nome": nome_cliente,
            "idade": idade_cliente
        }

        Commands.cria_arquivo_json(DICT_USER_SENHA, dados_login)
        
        tipo_de_conta = input('Aperte C para conta corrente ou P para conta Poupanca').upper().strip()

        if tipo_de_conta == 'C':
            cliente = pessoas.Cliente(id, nome_cliente, idade_cliente)
            conta_cliente = contas.ContaCorrente(123,222,0,100)
            cliente.conta = conta_cliente
            conta_cliente.id_user = id
            
            dados_conta_corrente = {
                "agencia": conta_cliente.agencia,
                "numero_conta": conta_cliente.numero_conta,
                "saldo": conta_cliente.saldo,
                "limite_extra": conta_cliente.limite_extra,
                "id_user": conta_cliente.id_user
            }

            Commands.cria_arquivo_json(DICT_CONTA, dados_conta_corrente)


        else:
            cliente = pessoas.Cliente(id, nome_cliente, idade_cliente)
            conta_cliente = contas.ContaPoupanca(456,333,0)
            cliente.conta = conta_cliente
            conta_cliente.id_user = id

            dados_conta_poupanca = {
                "agencia": conta_cliente.agencia,
                "numero_conta": conta_cliente.numero_conta,
                "saldo": conta_cliente.saldo,
                "id_user": conta_cliente.id_user
            }

            Commands.cria_arquivo_json(DICT_CONTA, dados_conta_poupanca)

if __name__ == '__main__':
    main()