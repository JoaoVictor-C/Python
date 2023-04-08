print('====== DESAFIO 49 ======')
num = int(input('Digite um número: '))
print('-=-'*10)
print('O número digitado foi {}.'.format(num))
print('Tabuada:')
valor = 0
for c in range(0, 10):
   valor += 1
   print('{} x  {} = {}'.format(num, valor,num*valor))
print('-=-'*10)