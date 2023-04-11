print('====== DESAFIO 57 ======')
sex = input('Qual é o seu sexo? [M] [F]\n')
if sex.upper() != 'M' and sex != 'F':
   while sex.upper() != 'M':
      sex = input('Valor digitado incorreto ou inválido, digite novamente\nQual é o seu sexo? [M] [F]\n').upper()
elif sex.upper() != 'F':
   while sex.upper() != 'F':
      sex = input('Valor digitado incorreto ou inválido, digite novamente\nQual é o seu sexo? [M] [F]\n').upper()
print('Sexo digitado {}'.format(sex))