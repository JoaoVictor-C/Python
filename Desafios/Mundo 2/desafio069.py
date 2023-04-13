print('===== DESAFIO 69 =====')
c = 0
while True:
   idade = int(input('Idade: '))
   if idade > 18:
      c += 1
   sexo = ' '
   while sexo not in 'MF':
      sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
   if sexo == 'M':
      c += 1
   if sexo == 'F' and idade < 20:
      c += 1
   resp = ' '
   while resp not in 'SN':
      resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
   if resp == 'N':
      break
print(f'Total de pessoas com mais de 18 anos: {c}')
print(f'Ao todo temos {c} homens cadastrados')
print(f'E temos {c} mulheres com menos de 20 anos')