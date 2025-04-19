def leiaint(txt):
    while True:
        try:
            entrada = int(input(txt))
        except TypeError as error:
            print(f'\033[0;31mClasse: {error.__class__}')
            print(f'\033[0;31mDescrição: Error com os Tipos de Dados digitados\033[m')
        except ValueError as error:
            print(f'\033[0;31mClasse: {error.__class__}')
            print(f'\033[0;31mDescrição: Erro com os Valores digitados\033[m')
        except TabError as error:
            print(f'\033[0;31mClasse: {error.__class__}')
            print(f'\033[0;31mDescrição: Erro pois você digitou muitos espaços\033[m')
        except KeyboardInterrupt as error:
            print(f'\033[0;31mClasse: {error.__class__}')
            print(f'\033[0;31mDescrição: Erro pois você não digitou este número\033[m')
            entrada = 0
            return entrada  
        else:
            print(f'\033[0;32m{entrada} é um número Inteiro!')
            return entrada

def leiafloat(txt):
    while True:
        try:
            entrada = float(input(txt))
        except TypeError as error:
            print(f'\033[0;31mClasse: {error.__class__}')
            print(f'\033[0;31mDescrição: Error com os Tipos de Dados digitados\033[m')
        except ValueError as error:
            print(f'\033[0;31mClasse: {error.__class__}')
            print(f'\033[0;31mDescrição: Erro com os Valores digitados\033[m')
        except TabError as error:
            print(f'\033[0;31mClasse: {error.__class__}')
            print(f'\033[0;31mDescrição: Erro pois você digitou muitos espaços\033[m')
        except KeyboardInterrupt as error:
            print(f'\033[0;31mClasse: {error.__class__}')
            print(f'\033[0;31mDescrição: Erro pois você não digitou este número\033[m')
            entrada = 0
            return entrada   
        else:
            print(f'\033[0;32m{entrada} é um número Real!')
            return entrada

li = leiaint('\033[0;37mDigite Número INTEIRO: ')
lf = leiafloat('\033[0;37mDigite Número REAL: ')
print(f'Número Inteiro: {li} número Real: {lf}')

#Por Emerson Machado 18/04/2025