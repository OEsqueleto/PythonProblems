print('BANCO EMERSON')
nota200 = nota100 = nota50 = nota20 = nota10 = nota5 = nota2 = moeda1 = 0
saque = int(input('Qual valor você quer saque? R$'))

while True:
    while saque // 200 != 0:
        nota200 = saque // 200
        saque = saque % 200
    while saque // 100 != 0:
        nota100 = saque // 100
        saque = saque % 100
    while saque // 50 != 0:
        nota50 = saque // 50
        saque = saque % 50
    while saque // 20 != 0:
        nota20 = saque // 20
        saque = saque % 20
    while saque // 10 != 0:
        nota10 = saque // 10
        saque = saque % 10
    while saque // 5 != 0:
        nota5 = saque // 5
        saque = saque % 5
    while saque // 2 != 0:
        nota2 = saque // 2
        saque = saque % 2 
    while saque // 1 != 0:
        moeda1 = saque // 1
        saque = saque % 1
        break
    break

print('SEU REGASTE:')
print(f'Total de {nota200} cédulas de 200')
print(f'Total de {nota100} cédulas de 100')
print(f'Total de {nota50} cédulas de 50')
print(f'Total de {nota20} cédulas de 20')
print(f'Total de {nota10} cédulas de 10')
print(f'Total de {nota5} cédulas de 5')
print(f'Total de {nota2} cédulas de 2')
print(f'Total de {moeda1} moedas de 1')
