fator = int(input('Qual é seu número fatorial?\n'))
resultado = 1
multi = str('')

for cont in range (fator,0,-1):
    resultado *= cont
    multi += str(cont) + ' x '

print('{}! = {} = {}'.format(fator, multi,resultado))

