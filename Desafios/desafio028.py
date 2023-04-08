import random
print('===== DESAFIO 28 =====')
valor = int(input('Digite um valor entre 1 e 5: '))
nAleatorio = random.randint(1,5)
if valor <= 5 and valor > 0:
   if valor == nAleatorio:
      print('Você acertou o número!')
      print('Valor digitado: {} | Valor aleatório: {}'.format(valor, nAleatorio))
   else:
      print('Você errou o número! O número escolhido foi {}.'.format(nAleatorio))
      print('Valor digitado: {} | Valor aleatório: {}'.format(valor, nAleatorio))
else:
   print('Insira um valor válido entre 1 e 5.')