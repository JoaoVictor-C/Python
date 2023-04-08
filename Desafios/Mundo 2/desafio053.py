print('====== DESAFIO 53 ======')
frase = input('Digite uma frase: ').strip().lower()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))