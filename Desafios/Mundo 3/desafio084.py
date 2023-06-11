pessoa = []
dados = []
peso = qtdP = 0
nome = ''
pesado = []
leve = []
while True:
    nome = str(input('Digite seu nome:\n> '))
    peso = int(input('Digite o seu peso:\n> '))
    dados.append(nome)
    if peso > 0:
        dados.append(peso)
    pessoa.append(dados[:])
    dados.clear()
    test = str(input('Quer cadastrar mais pessoas? [S] [N]\n> ')).upper()
    if test == 'N':
        break
    elif test == 'S':
        test == 'S'
    else:
         test = str(input('Você digitou o valor errado! Tente novamente.\nQuer cadastrar mais pessoas? [S] [N]\n> ')).upper()
         
for c in pessoa:
    qtdP += 1

print(f'Foram cadastradas {qtdP} pessoas!')

for pos, c in enumerate(pessoa):
    if pos == 0:
        pesado.append(c[0])
        pesado.append(c[1])
        leve.append(c[0])
        leve.append(c[1])
    if pos > 0:
        if pesado[-1] > c[1]:
            qtdP == 0
        elif pesado[-1] < c[1]:
            pesado.clear()
            pesado.append(c[0])
            pesado.append(c[1])
        elif pesado[-1] == c[1]:
            pesado.insert(0, c[0])
        if leve[-1] < c[1]:
            qtdP == 0
        elif leve[-1] > c[1]:
            leve.clear()
            leve.append(c[0])
            leve.append(c[1])
        elif leve[-1] == c[1]:
            leve.insert(0, c[0])

print(f'O maior peso foi de {pesado[0:-1]} pesando {pesado[-1]:.1f}Kg')
print(f'O menor peso foi de {leve[0:-1]} pesando {leve[-1]:.1f}Kg')