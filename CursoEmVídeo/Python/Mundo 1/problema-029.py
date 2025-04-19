vel = int(input('Qual é a velocidade do Carro? '))
conta = vel - 80
multa = conta * 7

if vel >= 81:
    print('MULTA! No valor de {}!'.format(multa))
else:
    print('LIBERADO! Continue dentro do limite!')
