soma = 0
velhoidade = 0
velhonome = str('')
mulheres = 0

for c in range (2):
    nome = str(input('Diga seu Nome: ')).strip().capitalize()
    idade = int(input('{}, Sua Idade: '.format(nome)))
    sexo = str(input('{}, Seu Sexo [M] ou [F]: '.format(nome))).strip().upper()
    soma += idade
    if sexo == 'M' and idade > velhoidade:
        velhoidade = idade
        velhonome = nome
    if sexo == 'F' and idade <= 20:
        mulheres += 1

media = soma/2

print('A média das idades é {}!'.format(media))
print('O homem mais velho se chama {}!'.format(velhonome))
print('A quantidade de mulhers com 20 anos ou menos é {}!'.format(mulheres))
