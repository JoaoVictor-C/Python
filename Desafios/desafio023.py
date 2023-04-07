print('===== DESAFIO 23 =====')
# valor = input('Digite um valor entre 0 e 9999: ')
# unidade = len(valor)
# print('Unidade: {}'.format(valor[unidade-1]))
# print('Dezena: {}'.format(valor[unidade-2]))
# print('Centena: {}'.format(valor[unidade-3]))
# print('Milhar: {}'.format(valor[unidade-4]))

valor = int(input('Digite um valor entre 0 e 9999: '))
unidade = valor // 1 % 10
dezena = valor // 10 % 10
centena = valor // 100 % 10
milhar = valor // 1000 % 10
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))