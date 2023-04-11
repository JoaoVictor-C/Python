'''for c in range(0, 5):
   n = int(input('Digite um valor: '))
print('Fim')'''
'''n = 1
while r == 'S':
   n = int(input('Digite um valor: '))
   r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')'''
n = 1
par = impar = 0
while n != 0:
   n = int(input('Digite um valor: '))
   if n == 0:
      break
   if n % 2 == 0:
      print(f'{n} é par')
      par += 1
   else:
      print(f'{n} é impar')
      impar += 1
print('Você digitou {} números pares e {} números impares'.format(par, impar))