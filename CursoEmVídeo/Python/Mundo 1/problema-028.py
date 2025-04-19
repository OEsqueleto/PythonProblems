from random import randrange
num = randrange(5)
user = int(input('Qual número EU estou pensando? '))
if user == num :
    print('Parabéns! Eu estava pensando no {}!'.format(num))
else:
    print('Não foi dessa vez! Eu estava pensando no {}!'.format(num))
