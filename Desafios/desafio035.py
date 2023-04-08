print('===== DESAFIO 35 =====')
print('Escreva o comprimento da primeira reta:')
reta1 = int(input())
print('Escreva o comprimento da segunda reta:')
reta2 = int(input())
print('Escreva o comprimento da terceira reta:')
reta3 = int(input())

if (reta1 + reta2) > reta3 and (reta2 + reta3) > reta1 and (reta3 + reta1) > reta2:
   print('Essas retas podem formar um triângulo!')
else:
   print('Essas retas não podem formar um triângulo!')