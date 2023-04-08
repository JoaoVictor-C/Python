import random
from time import sleep
print('===== DESAFIO 28 =====')
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5 tente advinhar...')
print('-=-' * 20)
valor = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(2)
nAleatorio = random.randint(0,5)
if valor <= 5 and valor > 0:
   if valor == nAleatorio:
      print('\033[1;32mParabéns! Você acertou o número!\033[m')
   else:
      print('\033[1;31mVocê perdeu! Eu pensei no número {}, e não no número {}!\033[m'.format(nAleatorio, valor))
else:
   print('Insira um valor válido entre 1 e 5.')