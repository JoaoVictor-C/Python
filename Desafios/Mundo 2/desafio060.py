print('===== DESAFIO 60 =====')
n2 = int(input('Insira um número inteiro: '))
n = n2
c = 1
while c < n2:
   n = n * (n2 - c)
   c += 1
print('O fatorial de {} é {}!'.format(n2, n))
   