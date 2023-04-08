print('===== DESAFIO 52 =====')
inp = int(input('Digite um número: '))
div = 0
val1 = 0
val2 = 0
for c in range(0, inp):
   div += 1
   if inp % div == 0:
      val1 += 1
   else:
      val2 += 1
if val1 == 2:
   print('É um número primo!')
else:
   print('Não é um número primo!')