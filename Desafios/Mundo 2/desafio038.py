print('===== DESAFIO 38 =====')
num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
if num1 > num2:
    print('O número \033[7;30m{}\033[m é maior que o número \033[7;30m{}\033[m'.format(num1, num2))
elif num2 > num1:
    print('O número \033[7;30m{}\033[m é maior que o número \033[7;30m{}\033[m'.format(num2, num1))
else:
    print('Os números \033[7;30m{}\033[m e \033[7;30m{}\033[m são iguais'.format(num1, num2))