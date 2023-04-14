print('===== DESAFIO 71 =====')
unidade = nota10 = nota100 = nota200 = nota50 = 0
while True:
   inpt = int(input('Digite um valor em reais a ser sacado: R$'))
   if inpt < 0:
      break
   unidade = inpt // 1 % 10
   dezena = inpt // 10 % 10 * 10
   centena = inpt // 100 * 10
   
   #inpt == 1340
   # centena == 130

   if dezena % 50 == 0:
      nota50 = dezena / 50
   elif dezena % 50 != 0:
      nota10 = dezena / 10
   
   if centena % 20 == 0:
      nota200 = centena / 20
   elif centena % 10 == 0:
      nota100 = centena / 100
   break
print(f'O valor digitado foi {inpt} será sacado \n{unidade} notas de R$1\n{nota10} notas de R$10\n{nota50:.0f} notas de R$50\n{nota100} notas de R$100\n{nota200:.0f} notas de R$200')