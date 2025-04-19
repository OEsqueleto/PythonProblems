print('DIGITE NÚMEROS!')
digitado = soma = quantidade = 0
digitado = int(input('De fato, apenas digite números:\n'))

while digitado != 999:
    soma += digitado
    quantidade += 1
    digitado = int(input('De fato, apenas digite números:\n'))

print('Último número digitad: {}!'.format(digitado))
print('Soma dos números é de: {}!'.format(soma))
print('Quantidade de números: {}!'.format(quantidade))
