print('====== DESAFIO 15 ======')
km = float(input('Digite a quantidade de KM rodado do carro: '))
dia = int(input('Digite a quantidade de dias que o carro foi alugado: '))
print('O total a pagar é: R$ {:.2f}!'.format((dia * 60)+(km * 0.15)))
