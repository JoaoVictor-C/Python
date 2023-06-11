par = []
impar = []

for c in range(0, 7):
    inpt = int(input('Digite um valor:\n> '))
    if inpt % 2 == 0:
        par.append(inpt)
    elif inpt % 2 == 1:
        impar.append(inpt)


par.sort()
impar.sort()

print(f'Os valores pares digitados foram:', end=' ')
for e in par:
    print(e, end=' ')
print(f'\nOs valores ímpares digitados foram:', end=' ')
for d in impar:
    print(d, end=' ')