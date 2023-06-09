num = []

teste = 'S'
qtd = 0

while True: 
    if teste == 'S':
        teste = 'S'
        
    elif teste == 'N':
        break
    
    else:
        teste = input('Valor inserido inválido!\nDeseja continuar? [S] [N]\n> ').upper()

    num.append(int(input('\nDigite um número:\n> ')))
    teste = input('Deseja continuar? [S] [N]\n> ').upper()
    
    
for c in num:
    qtd += 1
print(f'Foram adicionados {qtd} números à lista!')

num.sort(reverse=True)

print(f'Os números em ordem decrescente são: {num} ')

    
if 5 in num:
    print('O número 5 foi digitado e está na lista')