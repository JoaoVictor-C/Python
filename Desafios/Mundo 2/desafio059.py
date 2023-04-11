print('===== DESAFIO 58 =====')
n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
n = 0
while n != 5:
   n = int(input('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do progama\n'))
   if n == 1:
      print('A soma entre {} e {} é {}.'.format(n1, n2, n1+n2))
      res = input('Deseja voltar ao menu?  [S] [N]').upper()
      if res == 'S':
         n = 0
      else:
         break
   elif n == 2:
      print('O produto entre {} e {} é {}.'.format(n1, n2, n1*n2))
      res = input('Deseja voltar ao menu?  [S] [N]').upper()
      if res == 'S':
         n = 0
      else:
         break
   elif n == 3:
      if n1 > n2:
         print('O número {} é maior que {}.'.format(n1, n2))
      elif n2 > n1:
         print('O número {} é maior que {}.'.format(n2, n1))
      else:
         print('O número {} é igual ao número {}.'.format(n1, n2))
      res = input('Deseja voltar ao menu?  [S] [N]').upper()
      if res == 'S':
         n = 0
      else:
         break
   elif n == 4:
      n1 = int(input('Insira o primeiro número: '))
      n2 = int(input('Insira o segundo número: '))
   elif n == 5:
      break
   else:
      print('Número inserido inválido.')