c = numero = 0

while True:
    numero = int(input('\nQuer ver a tabuada de qual valor? '))
    if numero >= 0:
        c = 0
        while c != 10:
            print(f'{numero} x {c+1} = {numero*(c+1)}')
            c += 1
    else:
        break

print('Promgrama ENCERRADO! Número negativo inserido')