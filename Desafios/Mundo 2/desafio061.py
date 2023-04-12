print('===== DESAFIO 61 =====')
n = int(input('Digite o primeiro termo de uma PA: '))
f = int(input('Digite a sua razão: '))
p = 0
while p < 10:
   print('{}º: {}'.format(p+1, n+(f*p)))
   p += 1