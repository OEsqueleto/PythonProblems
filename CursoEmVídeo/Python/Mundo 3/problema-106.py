def ajuda(p):
    print(help)
    while True:
        palavra = input(f'\033[0;37m\nDigite sua Função: \033[1;32;40m')
        print(f'\033[1;34;47m{help(palavra)}')
        if palavra == 'fim':
            print('\033[1;33mFECHANDO PROGRAMA')
            return palavra

ajuda('\033[0;35mDigite sua Função: ')
#Por Emerson Machado 17/04/2025