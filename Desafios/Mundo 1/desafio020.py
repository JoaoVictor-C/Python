from random import shuffle

print('===== DESAFIO 20 =====')
g1 = input('Digite o nome do grupo 1: ')
g2 = input('Digite o nome do grupo 2: ')
g3 = input('Digite o nome do grupo 3: ')
g4 = input('Digite o nome do grupo 4: ')
lista = [g1, g2, g3, g4]
shuffle(lista)
print('O a ordem de grupos selecionados foi de: {}' .format(lista))
