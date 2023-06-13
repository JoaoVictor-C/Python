linha = [[], [], []]

for c in range(0, 3):
    for cont in range(0, 3):
        linha[c].append(int(input(f'Digite um número para ser adicionado na posição [{c}, {cont}]\n> ')))
        
print(linha[0])
print(linha[1])
print(linha[2])