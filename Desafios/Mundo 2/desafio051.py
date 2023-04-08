print('===== DESAFIO 51 =====')
n = int(input('Digite o primeiro termo de uma PA: '))
f = int(input('Digite a sua razão: '))
p = 0
for c in range(1, 10):
   p += 1
   print('{}º: {}.'.format(p, n+(f*p-1)))