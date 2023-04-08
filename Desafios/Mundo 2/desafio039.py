print('===== DESAFIO 39 =====')
from datetime import date
ano_atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
if ano_atual - nascimento < 18:
   print('Ainda faltam {} anos para o alistamento.'.format(18 - (ano_atual - nascimento)))
   print('Seu alistamento será em {}.'.format(ano_atual + (18 - (ano_atual - nascimento))))
elif ano_atual - nascimento == 18:
   print('Você tem que se alistar IMEDIATAMENTE!')