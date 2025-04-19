pessoas = []
for c in range (4):
    peso = int(input('Peso da {}° Pessoa: '.format(c+1)))
    pessoas.append({ 'peso':peso })

maior = max(pessoas, key=lambda pessoa: pessoa['peso'])
menor = min(pessoas, key=lambda pessoa: pessoa['peso'])
print(pessoas)
print('O MAIOR peso foi de {}Kg'.format(maior['peso']))
print('O MENOR peso foi de {}Kg'.format(menor['peso']))
