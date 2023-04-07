import math

print('===== DESAFIO 18 =====')
angle = float(input('Digite um número: '))
angle = math.radians(angle)
sen = math.sin(angle)
cos = math.cos(angle)
tng = math.tan(angle)
print('O ângulo de {:.0f}° tem o SENO de {:.2f}'.format(math.degrees(angle), sen))
print('O ângulo de {:.0f}° tem o COSENO de {:.2f}'.format(math.degrees(angle), cos))
print('O ângulo de {:.0f}° tem a TANGENTE de {:.2f}'.format(math.degrees(angle), tng))