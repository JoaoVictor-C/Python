print('===== DESAFIO 65 =====')
i = 0
t = 0
tN = 0
maior = 0
menor = 0
while i != 999:
   res = int(input('Digite um número, digite 999 para parar: '))
   if res == 999:
      break
   t += res
   tN += 1
   if tN == 1:
      maior = res
      menor = res
   else:
      if res > maior:
         maior = res
      if res < menor:
         menor = res
print('O total de números digitados foi: {}!\nA soma de todos os números foi de: {}!\nO maior número digitado foi: {}!\nO menor número digitado foi: {}!'.format(tN, t, maior, menor))
#Change the break to a continue question if user says S continue if user say N break