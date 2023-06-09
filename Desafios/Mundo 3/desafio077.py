palavras = ('Abacaxi', 'Banana', 'Cachorro', 'Dado', 'Elefante', 'Foca', 'Girafa', 'Hidrante', 'Ilha', 'Jacare', 'Kiwi', 'Laranja', 'Macaco', 'Nariz', 'Ovo', 'Pato', 'Queijo', 'Rato', 'Sapo', 'Tigre')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais  ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end='  ')