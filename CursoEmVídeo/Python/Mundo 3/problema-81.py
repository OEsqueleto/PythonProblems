lista = []
while True:
    números = int(input('Digite números: '))
    lista.append(números)
    resposta = str(input('Deseja continuar? [S/N] '))
    while resposta not in 'NnSs':
        print(f'ERRO: Você digitou {resposta}.')
        resposta = str(input('Deseja continuar? [S/N] '))
    if resposta in 'Nn':
        print('Saindo do Programa.')
        break
    
print(f'\nLista Completa: {lista}')    
print(f'Total de números digitados: {len(lista)}')
print(f'Lista em ordem decrescente: {sorted(lista, reverse=True)}')
if 5 in lista:
    print(f'5 Está na lista na posição {lista.index(5)+1}')
else:
    print('Infelizmente 5 não está na lista...')
