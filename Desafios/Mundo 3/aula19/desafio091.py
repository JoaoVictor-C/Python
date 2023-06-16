from random import randint
import time
resultado = dict()
mai = 0
ordenado = dict()
print('Jogadores sorteados:')
for c in range(0, 4):
    print(f'    O jogador {c+1} tirou o dado: ', end='')
    resultado[f'jogador{c+1}'] = randint(1, 6)
    print(resultado[f"jogador{c+1}"])
    time.sleep(1)
    
print('Ranking dos jogadores:')

