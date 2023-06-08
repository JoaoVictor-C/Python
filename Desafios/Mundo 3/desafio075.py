n1 = int(input('Digite um valor entre 1 e 10: \n> '))
n2 = int(input('Digite um valor entre 1 e 10: \n> '))
n3 = int(input('Digite um valor entre 1 e 10: \n> '))
n4 = int(input('Digite um valor entre 1 e 10: \n> '))

while True:
    if n1 < 1 or n1 > 10:
        n1 = int(input('Você digitou o primeiro valor errado! Digite novamente: \n> '))
    if n2 < 1 or n2 > 10:
        n2 = int(input('Você digitou o segundo valor errado! Digite novamente: \n> '))
    if n3 < 1 or n3 > 10:
        n3 = int(input('Você digitou o terceiro valor errado! Digite novamente: \n> '))
    if n4 < 1 or n4 > 10:
        n4 = int(input('Você digitou o quarto valor errado! Digite novamente: \n> '))
    
    if n1 >= 1 and n1 <= 10 and n2 >= 1 and n2 <= 10 and n3 >= 1 and n3 <= 10 and n4 >= 1 and n4 <= 10:
        break

numeros = (n1, n2, n3, n4)

qtd9 = 0
pos3 = 0
qtdPar = 0

print('Os numeros pares digitados foram:')
for pos, c in enumerate(numeros):
    if c == 9:
        qtd9 += 1

    if c == 3 and pos3 == 0:
        pos3 = pos
    
    if c % 2 == 0:
        print(c)

print(f'Foram digitados {qtd9} números 9!')
print(f'O número 3 foi digitado pela primeira vez na {pos3+1}º tentativa! E está na posição {pos3}.')