n1 = int(input('Digite um valor entre 1 e 10: \n> '))
n2 = int(input('Digite um valor entre 1 e 10: \n> '))
n3 = int(input('Digite um valor entre 1 e 10: \n> '))
n4 = int(input('Digite um valor entre 1 e 10: \n> '))

while True:
    if n1 < 1 or n1 > 10:
        print('Você digitou o primeiro valor errado!')
        n1 = int(input('Digite novamente: \n> '))
    if n2 < 1 or n2 > 10:
        print('Você digitou o segundo valor errado!')
        n2 = int(input('Digite novamente: \n> '))
    if n3 < 1 or n3 > 10:
        print('Você digitou o terceiro valor errado!')
        n3 = int(input('Digite novamente: \n> '))
    if n4 < 1 or n4 > 10:
        print('Você digitou o quarto valor errado!')
        n4 = int(input('Digite novamente: \n> '))
    
    if n1 >= 1 and n1 <= 10 and n2 >= 1 and n2 <= 10 and n3 >= 1 and n3 <= 10 and n4 >= 1 and n4 <= 10:
        break

numeros = (n1, n2, n3, n4)

print(f'Você digitou os números {numeros}')

if 9 in numeros:
    print(f'Foram digitados {numeros.count(9)} números 9!')
else:
    print('O número 9 não foi digitado!')
    
if 3 in numeros:
    print(f'O número 3 foi digitado pela primeira vez na {numeros.index(3)+1}º tentativa! E está na posição {numeros.index(3)}.')
else:
    print('O valor 3 não foi digitado!')
    
print('Os numeros pares digitados foram:', end='')
for c in numeros:
    if c % 2 == 0:
        print(c, end='')