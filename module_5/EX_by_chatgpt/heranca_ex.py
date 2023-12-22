# Exercício: Sistema de Pagamento

# Você está desenvolvendo um sistema de pagamento para uma empresa. Existem diferentes tipos de funcionários, cada um com sua própria forma de receber o salário. Implemente as classes necessárias usando herança para representar os diferentes tipos de funcionários.

#     Crie uma classe base chamada Funcionario com os atributos nome e salario.

#     Crie uma classe derivada chamada FuncionarioAssalariado, que herda da classe Funcionario. Essa classe deve ter um método chamado calcular_salario, que retorna o salário mensal fixo do funcionário assalariado.

#     Crie outra classe derivada chamada FuncionarioPorHora, que herda da classe Funcionario. Essa classe deve ter um método chamado calcular_salario, que recebe o número de horas trabalhadas e a taxa por hora, e retorna o salário correspondente.

#     Finalmente, crie uma classe derivada chamada FuncionarioComissionado, que herda da classe Funcionario. Essa classe deve ter um método chamado calcular_salario, que recebe o valor total das vendas realizadas pelo funcionário e a taxa de comissão, e retorna o salário correspondente.

# Lembre-se de criar instâncias das classes e testar os métodos para garantir que tudo está funcionando conforme o esperado.

# Dica: Utilize o método __init__ nas classes para inicializar os atributos.