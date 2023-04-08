print('===== DESAFIO 31 =====')
valor = int(input('Qual é a distância da viagem?\n'))
if valor < 201:
   print('Você viajou {}! O preço da passagem foi de: R${:.2f}'.format(valor, valor*0.5))
else:
   print('Você viajou {}! O preço da passagem foi de: R${:.2f}'.format(valor, valor*0.45))