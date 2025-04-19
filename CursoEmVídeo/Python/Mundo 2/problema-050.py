soma = 0
for total in range (0,6,1):
    num = int(input('Digite seu número PAR: '))
    if num % 2 == 0:
        soma += num
        
print('A soma é de: {}'.format(soma))
print('FIM')
