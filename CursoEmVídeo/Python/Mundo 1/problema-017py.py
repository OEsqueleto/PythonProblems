from math import hypot
oposto = float(input('Qual é seu cateto oposto? '))
adjacente = float(input('Qual é seu cateto adjacente? '))

hipotenusa = hypot(oposto,adjacente)

print('A hipotenusa é igual a {:.2f}'.format(hipotenusa))
