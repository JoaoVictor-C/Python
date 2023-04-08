print('====== DESAFIO 12 ======')
pç = float(input('Digite o preço de um produto: R$'))
print('O preço do produto é R${:.2f} com um desconto de 5% o preço fica R${:.2f}'.format(pç, (-pç*0.05) + pç))