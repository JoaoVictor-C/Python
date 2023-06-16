import datetime
cadastro = dict()
idade = 0
aposentadoria = 0
contribuicao = 0
now = datetime.datetime.now()
while True:
    cadastro['nome'] = str(input('Nome:\n> '))
    idade = int(input('Ano de Nascimento:\n> '))
    cadastro['idade'] = now.year - idade
    cadastro['ctps'] = int(input('Carteira de trabalho (0 caso não tenha):\n> ')) 
    if cadastro['ctps'] == 0:
        cadastro['ano de contratação'] = int(input('Ano de contratação:\n> '))
        cadastro['salario'] = int(input('Sálario:\n> '))
    aposentadoria = now.year - cadastro['ano de contratação']
    break
print('\n', '*-*' * 20)
print(cadastro)
print('\n', '*-*' * 20)

contribuicao = now.year - cadastro['ano de contratação']

if idade < 60:
    aposentadoria += 60 - idade

if aposentadoria + (now.year - cadastro['ano de contratação']) > 30
    aposentadoria += now.year - cadastro['ano de contratação']

