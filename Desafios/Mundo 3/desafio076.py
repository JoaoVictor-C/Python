print('===== DESAFIO 76 =====')
precos = (
   'Lápis', 1.75, 
   'Borracha', 2.00, 
   'Caderno', 15.90, 
   'Estojo', 25.00, 
   'Transferidor', 4.20, 
   'Compasso', 9.99, 
   'Mochila', 120.32, 
   'Canetas', 22.30, 
   'Livro', 34.90
)

print(10*'----')
print('           Listagem de Preços')
print(10*'----')

for pos, c in enumerate(precos):
   if pos % 2 == 0:
      print(f'{precos[pos]:.<30}R$ {precos[pos+1]:>6.2f}')