num = [[], []]

for c in range(0, 7):
    inpt = int(input('Digite um valor:\n> '))
    if inpt % 2 == 0:
        num[0].append(inpt)
    elif inpt % 2 == 1:
        num[1].append(inpt)


num[0].sort()
num[1].sort()

print(f'Os valores pares digitados foram:', end=' ')
for e in num[0]:
    print(e, end=' ')
print(f'\nOs valores ímpares digitados foram:', end=' ')
for d in num[1]:
    print(d, end=' ')