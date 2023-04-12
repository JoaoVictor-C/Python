print('===== DESAFIO 64 =====')
i = 0
t = 0
tN = 0
while i != 999:
   res = int(input('Digite um número, digite 999 para parar: '))
   if res == 999:
      break
   t += res
   tN += 1
print('O total de números digitados foi: {}!\nA soma de todos os números foi de: {}!'.format(tN, t))
   