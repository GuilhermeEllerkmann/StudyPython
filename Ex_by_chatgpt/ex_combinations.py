from itertools import combinations

# Exercício: Uma sala de aula tem 10 alunos. 
# O professor deseja formar um grupo de estudo com 3 alunos. 
# Quantas combinações diferentes de grupos o professor pode formar?

students = ['Joe','Erica','Katarina','Karen','Ashley','Alex','Igor','Fernado','Miguel','Julia']

amount_of_students = len(students)

disired_student_per_group = 3

quantity_of_combinations = list(combinations(range(1, amount_of_students + 1), disired_student_per_group))

print(len(quantity_of_combinations))