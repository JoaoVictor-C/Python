linha = [[], [], []]
par = 0
somaColuna3 = 0
for c in range(0, 3):
    for cont in range(0, 3):
        linha[c].append(int(input(f'Digite um número para ser adicionado na posição [{c}, {cont}]\n> ')))
        
print(linha[0])
print(linha[1])
print(linha[2])

for c in linha:
    for cont in range(0,3):
        if c[cont] % 2 == 0:
            par += c[cont]

for c in range(0,3):
    somaColuna3 += linha[c][2]

print(f'A soma de todos os valores pares digitados são {par}!')
print(f'A soma dos valores da terceira coluna são {somaColuna3}!')
print(f'O maior valor da segunda linha é {max(linha[1])}')