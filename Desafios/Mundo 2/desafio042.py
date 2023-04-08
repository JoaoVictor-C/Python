print('===== DESAFIO 42 =====')
reta1 = float(input('Comprimento da primeira reta: '))
reta2 = float(input('Comprimento da segunda reta: '))
reta3 = float(input('Comprimento da terceira reta: '))
if (reta1 + reta2) > reta3 and (reta2 + reta3) > reta1 and (reta3 + reta1) > reta2:
    print('Essas retas podem formar um triângulo!')
    if reta1 == reta2 == reta3:
        print('EQUILÁTERO')
    elif reta1 != reta2 != reta3 != reta1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Essas retas não podem formar um triângulo!')