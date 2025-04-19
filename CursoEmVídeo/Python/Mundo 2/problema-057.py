print('Bem vindo!')
sexo = str(input('Sexo: ')).strip().upper()


while sexo != 'M' and sexo != 'F':
    print('Oops você digitou "{}" Será que quis dizer "M" ou "F"? '.format(sexo))
    sexo = str(input('Sexo: ')).strip().upper()
    if sexo == '0':
        break
print('Parabéns você pode prosseguir! Sexo: {}'.format(sexo))
