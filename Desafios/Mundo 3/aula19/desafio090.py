aluno = dict()
aluno['nome'] = str(input('Digite seu nome:\n> '))
aluno['media'] = int(input('Digite a média do aluno:\n> '))

for k, v in aluno.items():
    print(f'{k} é igual a {v}')

if aluno['media'] < 7:
    print(f'O aluno {aluno["nome"]} com média {aluno["media"]} foi reprovado!' )
elif aluno['media'] >= 7:
    print(f'O aluno {aluno["nome"]} com média {aluno["media"]} foi aprovado!')