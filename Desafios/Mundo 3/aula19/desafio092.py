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
    if cadastro['ctps'] != 0:
        cadastro['ano de contratação'] = int(input('Ano de contratação:\n> '))
        cadastro['salario'] = int(input('Sálario:\n> '))
    break
print('\n', '*-*' * 20)
print(cadastro)
print('\n', '*-*' * 20)


aposentadoria += (now.year - cadastro['ano de contratação']) + (now.year - idade)
if (now.year - idade) >= 65 or  (now.year - cadastro['ano de contratação']) >= 35:
    cadastro['aposentadoria'] = 'pode se aposentar'
else:
    cadastro['aposentadoria'] = f'não pode se aposentar, falta {aposentadoria} anos'
for k, v in cadastro.items():
    print(f'O campo {k} tem valor {v}!')