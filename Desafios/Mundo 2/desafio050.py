print('====== DESAFIO 50 ======')
calc = 0
for c in range(0,6):
   valor = int(input('Insira um número inteiro: '))
   if valor % 2 == 0:
      calc += valor
print('A soma dos números pares digitados foi de: {}'.format(calc))