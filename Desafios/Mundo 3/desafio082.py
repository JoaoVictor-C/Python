from random import randint

n = []

par = []
impar = []

for cont in range(0, 10):
    n.append(randint(0,100))

for c in n:
    if c % 2 == 0:
        par.append(c)
    if c % 2 == 1:
        impar.append(c)
        
print(f'Todos os números inseridos:', end='')
for c in n:
    print(c, end=' ')

print(f'\nOs valores pares inseridos:', end='')
for c in par:
    print(c, end=' ')

print(f'\nOs valores ímpares inseridos:', end='')
for c in impar:
    print(c, end=' ')
