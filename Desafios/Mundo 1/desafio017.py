from math import hypot

print('===== DESAFIO 17 =====')
co = float(input('Digite o cateto oposto do retângulo: '))
ca = float(input('Digite o cateto adjacente do retângulo: '))
hip = hypot(co, ca)
print('O cateto adjacente é {:.2f} o cateto oposto é {:.2f} e a hipotenusa do retângulo é {:.2f}.'.format(ca, co, hip))
