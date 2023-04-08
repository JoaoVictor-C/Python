print('====== DESAFIO 54 ======')
from datetime import date
maior = 0
menor = 0
for i in range(1, 8):
    nasc = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(i)))
    atual = date.today().year
    idade = atual - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('{} pessoas são maiores de idade e {} são menores de idade.'.format(maior, menor))