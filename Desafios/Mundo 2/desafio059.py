print('===== DESAFIO 58 =====')
n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
n = 0
while n != 5:
   n = int(input('\033[1;33m[1]\033[m \033[36mSomar\033[m\n\033[1;33m[2]\033[m \033[36mMultiplicar\033[m\n\033[1;33m[3]\033[m \033[36mMaior\033[m\n\033[1;33m[4]\033[m \033[36mNovos números\033[m\n\033[1;33m[5]\033[m \033[36mSair do progama\033[m\n'))
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