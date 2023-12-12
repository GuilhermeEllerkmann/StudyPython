# Crie um programa em Python que receba uma lista de números como entrada e utilize a função filter para criar uma nova 
# lista contendo apenas os números pares. 
# Em seguida, imprima a lista original e a lista resultante contendo apenas os números pares.

list_of_numbers = [1,2,3,4,5,6,7,8,9,10]

def check_even(x):
    if x % 2 == 0:
        return x, 'par'
    

list_of_even = filter(
    check_even,
    list_of_numbers

)

print(list_of_numbers)
print(list(list_of_even))
