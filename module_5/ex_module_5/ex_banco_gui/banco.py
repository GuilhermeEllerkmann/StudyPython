


class Bancos:
    def __init__(self, contas = None, clientes = None, agencias = None):
        self.contas = contas or []
        self.clientes = clientes or []
        self.agencias = agencias or []

    def add_cliente_and_contas(self, clientes_, contas_):
        self.clientes.extend([clientes_])
        self.contas.extend([contas_])

    def add_agencias(self, *args):
        for i in args:
            self.agencias.extend([i])


    def checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            print('Agencia checada')
            return True
        else:
            print('Agencia nao correspondente')
            return False

    def checa_cliente(self, cliente):
        if cliente in self.clientes:
            print(f'cliente {cliente.nome} eh do banco')
            return True
        else:
            print(f'{cliente} n eh do banco')
            return False
        
    def checa_conta(self, conta):
        if conta in self.contas:
            print(f'conta {conta.numero_conta} eh do banco')
            return True
        else:
            print(f'conta {conta.numero_conta} n eh do banco')
            return False
        

    def _checa_se_conta_e_do_cliente(self, cliente, conta):
        if conta is cliente.conta:
            print('_checa_se_conta_e_do_cliente', True)
            return True
        print('_checa_se_conta_e_do_cliente', False)
        return False
    
    def autentica(self, cliente, conta):
        return self.checa_agencia(conta) and self.checa_cliente(cliente) and self.checa_conta(conta) and self._checa_se_conta_e_do_cliente(cliente, conta)


    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
        return f'{class_name}{attrs}'


