from random import choice

print('===== DESAFIO 19 =====')
a1 = str(input('Digite o aluno número 1: '))
a2 = str(input('Digite o aluno número 2: '))
a3 = str(input('Digite o aluno número 3: '))
a4 = str(input('Digite o aluno número 4: '))
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print('Foi sorteado o aluno {}!'.format(escolhido))