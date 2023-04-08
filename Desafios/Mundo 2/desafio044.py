print('===== DESAFIO 44 =====')
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] À Vista Dinheiro/Cheque
[2] À Vista Cartão
[3] 2x no Cartão
[4] 3x ou mais no Cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
   print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, preco - (preco * 10 / 100)))
elif opcao == 2:
   print('Sua compra de R${:.2f} vai custar R${:.2f}.'.format(preco, preco*0.95))
elif opcao == 3:
   print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS.'.format(preco / 2))
else:
   print('Sua compra será parcelada em 3x de R${:.2f} COM JUROS.'.format(preco * 1.2 / 3))