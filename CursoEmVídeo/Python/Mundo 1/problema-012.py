preco = int(input('Qual é o preço?'))
desconto = int(input('Qual é o desconto?'))

desco = desconto/100
valor = preco*desco
novo = preco-valor

print('{}R$ com {}% de desconto, é igual a: {}'.format(preco,desconto,novo))

#Por Emerson Machado 23/03/2025