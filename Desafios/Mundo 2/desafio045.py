print('===== DESAFIO 45 =====')
from random import randint
from time import sleep
print('Suas opções:')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
computador = randint(0, 2)
print('-=' * 11)
print('Computador jogou {}'.format(computador))
print('Jogador jogou {}'.format(jogador))
print('-=' * 11)
if jogador == 0 and computador == 2 or jogador == 1 and computador == 0 or jogador == 2 and computador == 1:
    print('JOGADOR VENCE!')
elif computador == 0 and jogador == 2 or computador == 1 and jogador == 0 or computador == 2 and jogador == 1:
    print('COMPUTADOR VENCE!')
else:
    print('EMPATE!')
