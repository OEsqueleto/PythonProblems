lista = []
adicionados = []

while True:
    lista.append(int(input('Adicone valores na lista: ')))
    if lista[-1] not in adicionados:
        adicionados.append(lista[-1]) 
    else:
        print(f'Valor {lista[-1]} é duplicado! Não será adicionado.')
    resposta = input(str('Deseja Continuar [S/N]? '))
    if resposta in 'SsNn':
        if resposta in 'Nn':
            print('\nFechando programa...\n')
            break
    else:
        input(f'Você digitou {resposta}.Apenas aceitamos S ou N ')
        
print(f'Valores que foram adicionados: {sorted(adicionados)}')
print(f'Todos os valores digitados: {lista}')
