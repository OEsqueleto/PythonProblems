def leiaint(txt):
    entrada = input(txt)
    while not entrada.isdigit():
        print(f'\033[0;31mERRO! "{entrada}" Não é um número inteiro!')
        entrada = input(txt)
    if entrada.isdigit():
        print(f'\033[0;32m{entrada} é um número inteiro!')
        return entrada

leiaint('\033[0;37mDigite seu Número: ')
#Por Emerson Machado 17/04/2025