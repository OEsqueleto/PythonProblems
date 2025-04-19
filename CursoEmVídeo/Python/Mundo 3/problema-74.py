from random import sample

sorteados = tuple(sample(range(0,101),5))
formatado = str(sorteados).replace("(","").replace(")","")
print(f'Os Números sorteados foram: {formatado}')
print(f'O maior número sorteado foi: {max(sorteados)}')
print(f'O menor número sorteado foi: {min(sorteados)}')
