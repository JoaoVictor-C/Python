print('====== DESAFIO 13 ======')
nome = str(input('Digite um nome: '))
sal = int(input('Digite a quantia que {} ganha: '.format(nome)))
print('{} ganha R${:.2f} entretanto, irá receber um aumento de 15%, logo {} irá ganhar R${:.2f}'.format(nome, sal, nome, (sal*0.15)+sal))