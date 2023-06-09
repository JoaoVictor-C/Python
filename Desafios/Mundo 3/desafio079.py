n = []
teste = 'ÇÇ'
while True:
    for c in n:
        if n.count(c) > 1:
            n.remove(c)
    if teste == 'ÇÇ':
        teste = 'ÇÇ'
    elif teste == 'S':
        teste = 'S'
    elif teste == 'N':
        break
    else:
        teste = input('Valor inserido inválido!\nDeseja continuar? [S] [N]\n> ').upper()
    if teste == 'ÇÇ':
        n.append(int(input('\nDigite um número:\n> ')))
    if teste != 'ÇÇ': 
        n.append(int(input('\nDigite um número:\n> ')))
    teste = input('Deseja continuar? [S] [N]\n> ').upper()
print(sorted(n))