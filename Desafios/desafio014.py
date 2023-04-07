print('====== DESAFIO 13 ======')
Celsius = float(input("Digite uma temperatura em C°: "))
print('A temperatura digita em graus celsius é de: {:.1f}°C! \nConvertida em fahrenheit: é de {:.2f}! \nConvertida em Kelvin é de: {:.2f}°F!'.format(Celsius, Celsius * 1.8 + 32, 273.15 + Celsius))
