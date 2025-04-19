conjunto = [[],[]]
num = 0
for c in range (1,8):
    num = int(input(f'Digite o {c}º número: '))
    if num % 2 == 0:
        conjunto[0].append(num)
    else:
        conjunto[1].append(num)
print(f'\nTodos números digitados: {conjunto}')
print(f'Números Pares: {sorted(conjunto[0])}')
print(f'Números Impares: {sorted(conjunto[1])}')
    