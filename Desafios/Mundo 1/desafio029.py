print('===== DESAFIO 29 =====')
velCar = int(input('Velocidade do carro: '))
velMax = 80
if velCar > velMax:
   valorMulta = (velCar-velMax)*7
   print('Você foi multado por ultrapassar o limite de velocidade!\nVelocidade máxima {}km/h velocidade do seu carro {}.\nValor da multa: R${}'.format(velMax, velCar, valorMulta))
else:
   print('Você está na velocidade permitida! Siga em frente')