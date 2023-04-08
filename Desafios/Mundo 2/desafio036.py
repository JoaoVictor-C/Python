print('===== DESAFIO 36 =====')
salario = float(input('Qual é o seu salário? R$'))
valCasa = float(input('Qual é o valor da casa? R$'))
qntdAnos = int(input('Quantos anos você quer pagar? '))

if salario*0.30 < valCasa/qntdAnos:
   print('O empréstimo foi negado! O sálario é insuficiente.')
else:
   pagamento = valCasa / qntdAnos
   print('Você consegue pagar a casa!\nO valor total da casa foi de R${:.2f} e você irá pagar mensalmente R${:.2f}'.format(valCasa, pagamento))