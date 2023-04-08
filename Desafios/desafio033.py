print('===== DESAFIO 33 =====')
print('Digite o primeiro valor:')
valor1 = int(input())
print('Digite o segundo valor:')
valor2 = int(input())
print('Digite o terceiro valor:')
valor3 = int(input())

if valor1 > valor2 and valor1 > valor3:
   print('O valor {} é o maior!'.format(valor1))
   if valor2 > valor3:
      print('O valor {} é o menor!'.format(valor3))
   else:
      print('O valor {} é o menor!'.format(valor2))
      
elif valor2 > valor1 and valor2 > valor3:
   print('O valor {} é o maior!'.format(valor2))
   if valor1 > valor3:
      print('O valor {} é o menor!'.format(valor3))
   else:
      print('O valor {} é o menor!'.format(valor1))
      
else:
   print('O valor {} é o maior!'.format(valor3))
   if valor1 > valor2:
      print('O valor {} é o menor!'.format(valor2))
   else:
      print('O valor {} é o menor!'.format(valor1))