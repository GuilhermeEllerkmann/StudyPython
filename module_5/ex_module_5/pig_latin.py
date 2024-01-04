# user recebe imput
# se ela comecar com uma vogal, retorna a palavra + -hay
# se a palavra n comecar com vogal, tira a primeira letra da palavra e colocar palavra_sem_a_primeira_letra-primeira_letra+tay

# carro - arro-tay
# amor = amor-hay
# twitter = witter-tay

user_imput = input('digite uma palavra somente: ')

if user_imput[0] in 'aeiouAEIOU': 
    print(user_imput + '-hay')
else:
    print(user_imput[1:] + f'-{user_imput[:1]}ay')