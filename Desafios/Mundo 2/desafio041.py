print('===== DESAFIO 41 =====')
from datetime import date
ano_atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
if ano_atual - nascimento <= 9:
   print('MIRIM')
elif ano_atual - nascimento <= 14:
   print('INFANTIL')
elif ano_atual - nascimento <= 19:
   print('JUNIOR')
elif ano_atual - nascimento <= 25:
   print('SÊNIOR')