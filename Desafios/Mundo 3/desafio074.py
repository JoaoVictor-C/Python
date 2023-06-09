from random import randint

n = (randint(1,99), randint(1,99), randint(1,99), randint(1,99), randint(1,99), randint(1,99), randint(1,99), randint(1,99), randint(1,99))

maior = 0
menor = 0

for pos, c in enumerate(n):
    if pos == 0:
        menor = n[pos]
        maior = n[pos]
        
    if n[pos] > maior:
        maior = n[pos]
        
    if n[pos] < menor:
        menor = n[pos]

print(f'Os números gerados foram: ', end='')
for c in n:
    print(f'{c} ', end='')
print(f'\nO menor numero foi {menor}')
print(f'O maior número foi {maior}')