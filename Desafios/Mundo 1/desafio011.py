print('====== DESAFIO 11 ======')
alt = int(input('Digite a altura da parade(m): '))
larg = int(input('Digite a largura da parede(m): '))
print
print('A largura da parede é {}m e a altura é {}m. \nA área da parede é: {}m². \nConsiderando que 1L = 2m², seriam necessários {} para pintar a parede.'.format(larg, alt, larg*alt, (larg*alt)/4))