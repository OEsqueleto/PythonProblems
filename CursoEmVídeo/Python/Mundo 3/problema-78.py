valores = []

for cont in range(0,5):
    valores.append(int(input(f'Digite o {cont}º valor: ')))

maiores = max(valores)
menores = min(valores)
posições_alto = [i for i, v in enumerate(valores) if v == maiores]
posições_bixo = [i for i, v in enumerate(valores) if v == menores]

print('--'*15)
print(f'Você digitou: {valores}')
print(f'Maior Valor: {max(valores)} na posição {", ".join(str(i) for i in (posições_alto))}')
print(f'menor valor: {min(valores)} na posição {", ".join(str(i) for i in (posições_bixo))}')
