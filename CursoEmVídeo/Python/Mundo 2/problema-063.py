print('BEM VINDO A SEQUÊNCIA FIBONACCI!')
total = int(input('Deseja ver quantos números? '))
cont = 0
a = 0
b = 1
c = 0

while cont != total:
    cont += 1
    print('{} + {} = {}'.format(a,b,c))
    a = b
    b = c
    c = a + b
print('FIM!')
