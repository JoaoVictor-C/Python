palavras = ('Abacaxi', 'Banana', 'Cachorro', 'Dado', 'Elefante', 'Foca', 'Girafa', 'Hidrante', 'Ilha', 'Jacare', 'Kiwi', 'Laranja', 'Macaco', 'Nariz', 'Ovo', 'Pato', 'Queijo', 'Rato', 'Sapo', 'Tigre')

for pos, c in enumerate(palavras):
    a = 'a '
    qtdA = palavras[pos].upper().count('A')
    
    e = 'e '
    qtdE = palavras[pos].upper().count('E')
    
    i = 'i '
    qtdI = palavras[pos].upper().count('I')
    
    o = 'o '
    qtdO = palavras[pos].upper().count('O')
    
    u = 'u '
    qtdU = palavras[pos].upper().count('U')
    
    print(24*'--')
    print(f'\nNa palavra {palavras[pos].upper()} temos as vogais ', qtdA*a, qtdE*e, qtdI*i, qtdO*o, qtdU*u, '\n')
    print(24*'--')