# Exercício: Sistema de Pagamento

# Você está desenvolvendo um sistema de pagamento para uma empresa. Existem diferentes tipos de funcionários, cada um com sua própria forma de receber o salário. 
# Implemente as classes necessárias usando herança para representar os diferentes tipos de funcionários.

#     Crie uma classe base chamada Funcionario com os atributos nome e salario.

#     Crie uma classe derivada chamada FuncionarioAssalariado, que herda da classe Funcionario. Essa classe deve ter um método chamado calcular_salario, 
        # que retorna o salário mensal fixo do funcionário assalariado.

#     Crie outra classe derivada chamada FuncionarioPorHora, que herda da classe Funcionario. Essa classe deve ter um método chamado calcular_salario, 
        # que recebe o número de horas trabalhadas e a taxa por hora, e retorna o salário correspondente.

#     Finalmente, crie uma classe derivada chamada FuncionarioComissionado, que herda da classe Funcionario. 
        # Essa classe deve ter um método chamado calcular_salario, que recebe o valor total das vendas realizadas pelo funcionário e a taxa de comissão, e retorna o salário correspondente.

# Lembre-se de criar instâncias das classes e testar os métodos para garantir que tudo está funcionando conforme o esperado.

# Dica: Utilize o método __init__ nas classes para inicializar os atributos.r


class Employee():

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class SalariedEmployee(Employee):

    def __init__(self, name, salary):
        super().__init__(name, salary)

    def calc_salary(self):
        return f'the employee {self.name} is a {self.__class__.__name__} and this type of employee has a fixed salary of {self.salary}'
    

class PerHourEmployee(Employee):
    
    def __init__(self, name, salary, worked_hours, value_per_hour):
        super().__init__(name, salary)
        self.worked_hours = worked_hours
        self.value_per_hour = value_per_hour

    def calc_salary(self):
        return f'The employee {self.name} is a {self.__class__.__name__}. He worked {self.worked_hours} hours, and the value of an hour is {self.value_per_hour}, so his final salary is {self.worked_hours * self.value_per_hour}'
    
class PerComissionEmployee(Employee):

    def __init__(self, name, salary, value_per_sale, total_sales, tax_per_sale):
        super().__init__(name, salary)
        self.value_per_sale = value_per_sale
        self.total_sales = total_sales
        self.tax_per_sale = tax_per_sale

    def calc_salary(self):
        sales_total = self.total_sales * self.value_per_sale
        comission = (self.tax_per_sale / 100) * sales_total
        return f'The employee {self.name} is a {self.__class__.__name__}. He selled ${sales_total}, and his tax comission is {self.tax_per_sale}. So his final salary is ${comission}'
    
empregado = PerComissionEmployee('Gui', None, 50, 30, 25)
print(empregado.calc_salary())