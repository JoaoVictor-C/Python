print('===== DESAFIO 67 =====')
c = 0
while True:
   inp = int(input('Digite um número [negativo para parar]: '))
   if inp < 0:
      break
   for i in range(1, 11):
      print(f'{inp} x {i} = {inp * i}')
