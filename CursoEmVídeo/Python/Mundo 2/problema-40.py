nota1 = float(input('\033[mDigite a primeira nota: '))
nota2 = float(input('\033[mDigite a segunda nota: '))

media = (nota1 + nota2)/2

if media >= 7.0:
    print('\033[1;32mAPROVADO! Você passou com {}, parabéns!'.format(media))
elif media <= 5:
    print('\033[1;31mREPROVADO! Sua nota foi de {}, infelizmente...'.format(media))
else: print('\033[1;33mRECUPERAÇÃO! Sua nota foi de {}, atenção!'.format(media))
 