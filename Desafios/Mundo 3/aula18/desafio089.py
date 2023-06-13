boletim = []
cadastro = []
inpt = 'S'
while True:
    if inpt == 'N':
        break
    elif inpt == 'S':
        inpt == 'S'
    else:
        inpt = str(input('Valor inserido inválido ou incorreto. Tente novamente.\nDeseja cadastrar mais alunos? [S] [N]\n> ')).upper()
    cadastro.append(str(input('Digite o nome do aluno:\n> ')))
    cadastro.append(int(input('Digite a primeira nota do aluno:\n> ')))
    cadastro.append(int(input('Digite a segunda nota do aluno:\n> ')))
    inpt = str(input('Deseja cadastrar mais alunos? [S] [N]\n> ')).upper()
    boletim.append(cadastro[:])
    cadastro.clear()

for pos, c in enumerate(boletim):
    print(f'O aluno {c[0]} com ID #{pos+1} fechou com média {((c[1] + c[2]) / 2):.1f}!')

while True:
    inpt = str(input('Deseja ver as notas de algum aluno? [S] [N]\n> ').upper())
    if inpt == 'N':
        break
    elif inpt == 'S':
        inpt2 = int(input('Digite o id do aluno para ver a média!'))
        for pos, c in enumerate(boletim):
            if inpt2 == pos+1:
                print(f'O aluno {c[0]} tirou as notas {c[1]} e {c[2]}.')
    else:
        inpt = str(input('Valor inserido inválido. Tente novamente\nDeseja ver as notas de algum aluno? [S] [N]\n> ').upper())