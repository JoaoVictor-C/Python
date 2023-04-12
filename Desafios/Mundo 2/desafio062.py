print('===== DESAFIO 62 =====')
n = int(input('Digite o primeiro termo de uma PA: '))
f = int(input('Digite a sua razão: '))
p = 0
qtdF = -10
while p < 10:
   print('{}º: {}'.format(p+1, n+(f*p)))
   p += 1
if p == 10:
   res = input('Deseja mostrar mais termos dessa PA?    [S]  [N]\n').upper()
   if res == 'S':
      qtdF = int(input('Quantos termos você deseja mostrar? '))
if qtdF != -1:
   p = 0
   while p < (qtdF + 10):
      print('{}º: {}'.format(p+1, n+(f*p)))
      p += 1