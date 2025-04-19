print('!MÁQUINA DE CALCULAR!')
a = float(input('1° Número: '))
b = float(input('2° Número: '))

operar = int(input('[1]SOMAR\n[2]MULTIPLICAR\n[3]MAIOR\n[4]NOVOS NÚMEROS\n[5]SAIR\n'))

while operar != 5:
    if operar == 1:
        print(a+b)
        operar = int(input('[1]SOMAR\n[2]MULTIPLICAR\n[3]MAIOR\n[4]NOVOS NÚMEROS\n[5]SAIR\n'))
    elif operar == 2:
        print(a*b)
        operar = int(input('[1]SOMAR\n[2]MULTIPLICAR\n[3]MAIOR\n[4]NOVOS NÚMEROS\n[5]SAIR\n'))
    elif operar == 3:
        print(max(a,b))
        operar = int(input('[1]SOMAR\n[2]MULTIPLICAR\n[3]MAIOR\n[4]NOVOS NÚMEROS\n[5]SAIR\n'))
    elif operar == 4:
        a = float(input('1° Número: '))
        b = float(input('2° Número: '))
        operar = int(input('[1]SOMAR\n[2]MULTIPLICAR\n[3]MAIOR\n[4]NOVOS NÚMEROS\n[5]SAIR\n'))
    else:
        print('Oops, Acho que você digitiu errado {}...'.format(operar))
        operar = int(input('[1]SOMAR\n[2]MULTIPLICAR\n[3]MAIOR\n[4]NOVOS NÚMEROS\n[5]SAIR\n'))
print('Você SAIU da MÁQUINA DE CÁLCULAR!')