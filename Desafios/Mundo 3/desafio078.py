num = []
for cont in range(0,5):
    num.append(int(input('Digite um número inteiro:\n> ')))
    
menor = min(num)
maior = max(num)

print(f'O maior número digitado foi {maior} nas posições', end=' ')
for c in range(0, num.count(maior)):
    print(num.index(maior), end=' ')
    num[num.index(maior)] = 0

print(f'\nO menor número digitado foi {menor} nas posições', end=' ')
for c in range(0, num.count(menor)):
    print(num.index(menor), end=' ')
    num[num.index(menor)] = menor+1
