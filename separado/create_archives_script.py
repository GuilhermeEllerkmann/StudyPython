tamanho  = range(104, 172)
for x in tamanho:
    with open(f'aula{x}.py', 'w') as arquivo:
        arquivo.write(f'aula{x}')