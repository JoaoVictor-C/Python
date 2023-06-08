cont = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
extenso = ('Zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

logic = True

inpt = int(input('Digite um número inteiro entre 0 e 20: \n> '))

while logic == True:
    if inpt < 0 or inpt > 20:
        inpt = int(input('Número digitado incorreto ou inválido, digite outro número entre 1 e 20: \n> '))
    if inpt >= 0 and inpt <= 20:
        for c in cont:
            if c == inpt:
                print(f'Você digitou o número {cont[c]}!\nO número digitado por extenso foi: {extenso[c]}')
                logic = False