coletivo = []
individuo = {}
mulher = []
media = 0
velho = ['nome',0]

while True: 
    individuo['nome'] = str(input('Nome: '))
    individuo['sexo'] = str(input('Sexo: '))
    while individuo['sexo'] not in 'MmFf':
        individuo['sexo'] = str(input(f'Você digitou {individuo['sexo']}. Tente novamente, com M ou F '))
    individuo['idade'] = int(input('Idade: '))
    media += individuo['idade']
    coletivo.append(individuo.copy())
    resposta = str(input('Deseja continuar, [S/N]? '))
    while resposta not in 'SsNn':
        resposta = str(input(f'Você digitou {resposta}. Deseja Continuar [S/N]? '))
    if resposta in 'Nn':
        print('Fechando as perguntas... \n')
        break
    
print(coletivo)
print(individuo)    
for individuo in coletivo:
    if individuo['sexo'] in 'Ff':
        mulher.append(individuo['nome'])
    if individuo['idade'] >= velho[-1]:
        velho[0] = (individuo['nome'])
        velho[1] = (individuo['idade'])

print(f'Foram cadastradas {len(coletivo)} pessoas')
print(f'A média de idade é de {media/len(coletivo):.2f} anos')
print(f'As mulheres cadastradas foram: {" e ".join(mulher)}')
print(f'A pessoa mais velha é: {" com ".join([str(velho[0]), str(velho[1])])}')

#Por Emerson Machado 15/04/2025