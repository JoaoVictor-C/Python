import random
print('===== DESAFIO 68 =====')
c = 0
print('-\033[34m=\033[m-' * 15)
print('Vamos jogar par ou ímpar!')
print('-\033[34m=\033[m-' * 15)
while True:
      escolha = str(input('Par ou Ímpar? [P/I] ')).upper()
      if escolha != 'P' and escolha != 'I':
            print('Opção inválida!')
            continue
      n = int(input('Digite um número entre 0 e 10: '))
      computador = random.randint(0, 10)
      if n < 0 or n > 10:
            print('Opção inválida!')
            continue
      if n + computador % 2 == 0:
            if escolha == 'P':
                  print(f'Você venceu! O computador escolheu {computador}! {n} + {computador} = {n + computador} é par!')
                  c += 1
            if escolha == 'I':
                  print(f'Você perdeu! O computador escolheu {computador}! {n} + {computador} = {n + computador} é Ímpar!')
                  break
      if n + computador % 2 != 0:
            if escolha == 'I':
                  print(f'Você venceu! O computador escolheu {computador}! {n} + {computador} = {n + computador} é Ímpar!')
                  c += 1
            if escolha == 'P':
                  print(f'Você perdeu! O computador escolheu {computador}! {n} + {computador} = {n + computador} é par!')
                  break
print(f'Você venceu {c} vezes!')