from random import randint
resultado = dict()

for c in range(0, 4):
    print(f'O jogador {c+1} tirou o dado: ', end='')
    resultado[f'jogador{c}'] = randint(1, 6)
    print(resultado[f"jogador{c}"])

for c in range(0,1):
    for v in resultado.values():
        if c == 0:
            mai = v
        else:
            