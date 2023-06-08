from random import randint

n = (randint(1,999), randint(1,999), randint(1,999), randint(1,999), randint(1,999))
print(n)

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

print(f'Os números gerados foram: {n}')
print(f'O menor numero foi {menor}')
print(f'O maior número foi {maior}')