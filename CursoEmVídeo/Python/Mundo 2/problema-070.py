print('\nMAGAZINE LUIZA, MÓVEIS!')
resposta = str('S').strip().upper()
preço = quant = total = 0 
barato_preço = float(9999999)
barato_nome = nome = str('')

while resposta == 'S':
    nome = str(input('Nome: ')).strip().lower()
    preço = float(input('Preço: '))
    total += preço
    if preço >= 1000:
        quant += 1
    if preço < barato_preço:
        barato_nome = nome
        barato_preço = preço
    resposta = str(input('Vamos continuar? [S] ou [N]?\n')).strip().upper()
    if resposta == 'N':
        break
    while resposta not in 'SN':
        resposta = str(input(f'Você digitou "{resposta}".Mas só aceitamos [S] ou [N]\n')).strip().upper()

print('\nNO CAIXA!')
print(f'O custo total da compra foi de R${total:.2f}')
print(f'Temos {quant} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato_nome} custando R${barato_preço:.2f}!')
