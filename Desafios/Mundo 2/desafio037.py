print('===== DESAFIO 37 =====')
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para \033[7;30mBINÁRIO\033[m
[ 2 ] converter para \033[7;30mOCTAL\033[m
[ 3 ] converter para \033[7;30mHEXADECIMAL\033[m''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para \033[7;30mBINÁRIO\033[m é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para \033[7;30mOCTAL\033[m é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para \033[7;30mHEXADECIMAL\033[m é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')