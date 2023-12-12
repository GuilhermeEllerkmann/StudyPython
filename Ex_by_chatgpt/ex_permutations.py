from itertools import permutations

# Exercício: Uma equipe de futebol tem 11 jogadores. 
# O técnico precisa escolher a ordem dos jogadores para a formação inicial. 
# Quantas permutações diferentes de formações iniciais o técnico pode escolher?

players = ['1','2','3','4','5','6','7','8','9','10','11',]

amount_of_formations = print(len(list(permutations(players))), sep='\n')