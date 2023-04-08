print('====== DESAFIO 56 ======')
from datetime import date
soma_idade = 0
maior_idade_homem = 0
nome_velho = ''
mulheres_menos_20 = 0
for i in range(1, 5):
   print('----- {}ª PESSOA -----'.format(i))
   nome = str(input('Digite o nome da {}ª pessoa: '.format(i)))
   nasc = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(i)))
   sexo = str(input('Digite o sexo da {}ª pessoa: '.format(i)))
   atual = date.today().year
   idade = atual - nasc
   soma_idade += idade
   if sexo == 'M' or sexo == 'm':
      if idade > maior_idade_homem:
         maior_idade_homem = idade
         nome_velho = nome
   elif sexo == 'F' or sexo == 'f':
      if idade < 20:
         mulheres_menos_20 += 1
media_idade = soma_idade / 4
print('A média de idade do grupo é de {} anos.'.format(media_idade)) if media_idade > 0 else print('Não há pessoas no grupo.')
print('O homem mais velho tem {} anos e se chama {}.'.format(maior_idade_homem, nome_velho)) if maior_idade_homem > 0 else print('Não há homens no grupo.')
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulheres_menos_20)) if mulheres_menos_20 > 0 else print('Não há mulheres no grupo.')