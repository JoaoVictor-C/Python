n = []

n.append(input('Digite uma expressão qualquer (ex:  ((2+3)*2)  )\n> '))

if n[0].count('(') != n[0].count(')'):
    print("Sua expressão está errada!")
    
elif n[0].count('(') == n[0].count(')'):
    print('Sua expressão está correta!')