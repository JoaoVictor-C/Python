print('===== DESAFIO 48 =====')
valor = 0
for c in range(0, 500, 3):
   valor += 3
   if valor % 2 == 1 and valor < 501:
      print(valor)
print('Fim')