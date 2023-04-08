print('====== DESAFIO 8 ======')
m = float(input('Digite um valor em metros (M): '))
print('O valor digitado foi {}m. \n{}km \n{}hm \n{}dam \n{:.2f}dm \n{:.2f}cm \n{:.2f}mm'.format(m, m/1000, m/100, m/10, m*10, m*100, m*1000))