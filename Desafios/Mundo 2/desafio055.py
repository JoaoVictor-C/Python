print('====== DESAFIO 55 ======')
from datetime import date
maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(i)))
    if peso > maior:
        maior = peso
    if menor == 0:
        menor = peso
    elif peso < menor:
        menor = peso
print('O maior peso é {} e o menor é {}.'.format(maior, menor))