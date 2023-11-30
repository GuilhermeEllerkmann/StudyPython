# Crie um programa em Python que receba uma lista de números como entrada e use a função map para calcular o quadrado de cada número na lista. 
# Em seguida, imprima a lista original e a lista resultante com os quadrados.

list_of_numbers = [1,2,3,4,5,6,7,8,9]

print(list(map(lambda x: x * x, list_of_numbers)))