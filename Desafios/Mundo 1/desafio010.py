print('====== DESAFIO 10 ======')
din = float(input('Digite uma quantia em reais: R$'))
print('O valor digitado foi R${:.2f}. \nCom essa quantia você consegue comprar US${:.2f}. (Considerando cotação: US$1,00 = R$5,08)'.format(din, din/5.08))