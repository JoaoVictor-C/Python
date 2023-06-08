times = ("Atlético Mineiro", "Palmeiras", "Fortaleza", "Flamengo", "Bragantino", "Athletico Paranaense", "Bahia", "Corinthians", "Fluminense", "Santos", "Ceará", "Juventude", "Internacional", "Cuiabá", "São Paulo", "América Mineiro", "Sport Recife", "Grêmio", "Chapecoense", "Atlético Goianiense")

print('Os primeiros 5 colocados são:\n')
for c in range(0, 5):
    print(f'{c+1}º {times[c]}')
    
print('\n')
print(20*'-=-')
print('\n')

print('Os últimos 4 colocados são:\n')
for c in range(16, 20):
    print(f'{c+1}º{times[c]}')
    
print('\n')
print(20*'-=-')
print('\n')

print('Os 20 times em ordem alfabética: ')
print(f'{sorted(times)}')

print('\n')
print(20*'-=-')
print('\n')

for pos, c in enumerate(times):
    if c == 'Chapecoense':
        print(f'O time Chapecoense está na posição {pos}º')