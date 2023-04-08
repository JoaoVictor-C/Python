print('===== DESAFIO 24 =====')
cidade = input('Digite o nome de uma cidade: ').upper().strip()
print('A cidade {} começa com a palavra "SANTO"? {}'.format(cidade, cidade[:5] == 'SANTO'))