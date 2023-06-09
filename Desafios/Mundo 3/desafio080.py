from random import randint


num = []
inpt = 0

maior = 0
menor = 0

for c in range(0, 1000):
    if c == 0: 
        num.append(randint(0, 999))
    if c > 0:
        inpt = int(randint(0, 999))
        for pos, n in enumerate(num):
            if inpt > num[pos]:
                maior += 1
        num.insert(maior, inpt)
        maior = 0
        
print(num)