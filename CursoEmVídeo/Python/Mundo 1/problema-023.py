num = str(input('Digite seu número: '))
txt = num.zfill(4)
print('Número é {}'.format(txt))
print('Unidade: {}'.format(txt[3]))
print('Dezena:  {}'.format(txt[2]))
print('Centena: {}'.format(txt[1]))
print('Milhar:  {}'.format(txt[0]))

