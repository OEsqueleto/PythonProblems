lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite números: ')))
    resposta = str(input('Quer Continuar? [S] Sim ou [N] Não? '))
    while resposta not in 'SsNn':
        print(f'ERRO: Você digitou {resposta}.')
        resposta = str(input('Quer continuar? [S] ou [N]'))
    if resposta in 'Nn':
        print('\nSaindo do Programa...\n')
        break
for item in lista:
    if item % 2 == 0:
        par.append(item)
    else:
        impar.append(item)
print(f'Lista completa: {lista}')
print(f'Números Pares: {par}')
print(f'Números Ímpares: {impar}')
