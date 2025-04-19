num1 = float(input('\033[mDigite um número: '))
num2 = float(input('\033[mDigite OUTRO número: '))

if num1 == num2:
    print('\033[1;33mOs números {:.2f} e {:.2f} são IGUAIS!'.format(num1, num2))
elif num1 >= num2:
    print('\033[1;34mO número {:.2f} é MAIOR que o {:.2f}!'.format(num1, num2))
else: 
    print('\033[1;35mO número {:.2f} é MENOR que o {:.2f}!'.format(num1, num2))
     