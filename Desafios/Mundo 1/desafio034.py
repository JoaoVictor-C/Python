print('===== DESAFIO 34 =====')
salario = int(input('Qual é o seu salário?\n'))
if salario > 1250:
   print('O seu salário era de R${:.2f} porém após o aumento ele agora é de R${:.2f}.'.format(salario, salario*1.10))
else:
   print('O seu salário era de R${:.2f} porém após o aumento ele agora é de R${:.2f}.'.format(salario, salario*1.15))