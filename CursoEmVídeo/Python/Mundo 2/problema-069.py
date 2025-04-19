print('\nCADASTRO DE PESSOAS')
homem = mulheres = pessoas = 0
while True:
    print(f'\nCADASTRO DA {pessoas}° PESSOA:')
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).strip().upper()
    while sexo not in 'MF':
        print(f'Você digitiu sexo como "{sexo}", tente novamente...')
        sexo = str(input('Sexo: ')).strip().upper()
    if sexo in 'MF':
        if idade >= 18:
            pessoas += 1
        if sexo == 'M':
            homem += 1
        if sexo == 'F' and idade <= 20:
            mulheres += 1
        resposta = str(input('Quer continuar? [S] ou [N]?\n')).strip().upper()
        if resposta == 'N':
            break
        while resposta not in 'SN':
            resposta = str(input(f'Você digitou "{resposta}".Mas só aceitamos [S] ou [N]\n')).strip().upper()
print('\nFIM DO CADASTRO ')
print(f'Total de pessoas com mais de 18 anos: {pessoas} ')
print(f'Total de Homens cadastrados: {homem} ')
print(f'Mulheres com menos de 20 anos: {mulheres} ')
