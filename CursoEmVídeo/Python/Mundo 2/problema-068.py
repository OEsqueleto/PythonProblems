from random import randint
vitória = numjoga = 0
print('\nJOGO: PAR OU IMPAR!')

while numjoga in range (0,5): 
    tipo = str(input('\nQuer Par ou Impar? ')).strip().lower()
    numjoga = int(input('Escolha seu número de 0 a 5 '))
    bot = randint(0,5)
    resultado = numjoga + bot
    print (f'Hmm... Eu escolho {bot}')
    if resultado % 2 == 0:
        print('Deu PAR!')
        if tipo == 'par':
            print(f'Parabéns você VENCEU! Pois {numjoga} + {bot} é Par!\nVamos jogar mais uma vez!')
            vitória += 1
        else:
            print(f'Oops você Perdeu... Pois {numjoga} + {bot} é Par!')
            break
    else:
        print('Deu IMPAR!')
        if tipo == 'impar':
            print(f'Parabéns você VENCEU! Pois {numjoga} + {bot} é Impar!\nVamos jogar mais uma vez!')
            vitória += 1
        else:
            print(f'Oops você Perdeu... Pois {numjoga} + {bot} é Impar!')
            break

print ('\n\nGAME OVER!')
print (f'Você ganhou {vitória} vezes')
print (f'Sua última escolha foi {tipo} e {numjoga}!')
