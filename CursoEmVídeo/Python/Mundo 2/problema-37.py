texto = int(input('\033[mDIgite seu número: '))
print('BASE DE CONVERSÃO:\n [1] Binário\n [2] Octal\n [3] Hexadecimal')
base = int(input('Qual é a sua base? '))

if base == 1:
    print('Convertido em BINÁRIO:\n {}'.format(bin(texto) [2:]))
elif base == 2:
    print('Convertido em OCTAL:\n {}'.format(oct(texto) [2:]))
elif base == 3:
    print('Convertido em HEXADECIMAL:\n {}'.format(hex(texto) [2:]))
else:
    print('\033[1;31m VOCÊ NÃO DIGITOU UMA BASE VÁLIDA! {}'.format(base))
