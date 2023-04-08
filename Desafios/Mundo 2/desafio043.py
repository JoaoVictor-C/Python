print('===== DESAFIO 43 =====')
peso = float(input('Peso: '))
altura = float(input('Altura: '))
imc = peso / (altura ** 2)
if imc < 18.5:
   print('Abaixo do peso')
elif imc >= 18.5 and imc < 25:
   print('Peso ideal')
elif imc >= 25 and imc < 30:
   print('Acima do peso')