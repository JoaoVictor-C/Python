print('===== DESAFIO 66 =====')
c = 0
while True:
   n = int(input('Digite um número [999 para parar]: '))
   if n == 999:
      break
   c += n
print(f'A soma dos números digitados é {c}')