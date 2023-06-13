from random import randint
megaSena = []
palpites = []
jogos = int(input("Quantos jogos serão sorteados?\n> "))
while True:
    if jogos <= 0:
        jogos = int(input("Valor inserido inválido. Tente novamente\nQuantos jogos serão sorteados?\n> "))
    else:
        break
for c in range(0, jogos):
    for cont in range(0, 6):
        palpites.append(randint(1, 60))
    megaSena.append(palpites[:])
    palpites.clear()

print(f'Os jogos sorteados foram:',)
megaSena.sort()
for pos, c in enumerate(megaSena):
    print(f'Jogo {pos+1}: {c}')