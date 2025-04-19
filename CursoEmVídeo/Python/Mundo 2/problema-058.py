from random import randint

print('JOGO DA ADIVINHAÇÃO')
print('Estou pensando em um número entre 0 e 10')

computer = randint(0,10)
user = int(input('Meu palpite: '))
contador = 0

while user != computer:
    print('Você ERROU! Eu não estou pensando no {}!!'.format(user))
    user = int(input('No que estou pensando? '))
    contador += 1

print('Você ACERTOU! Eu pensei no {}! Você teve {} Palpites'.format(computer,contador))
