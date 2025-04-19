termo = int(input('Termo: '))
razao = int(input('Razão: '))
total = int(input('Total: '))
cont = 0

while cont != total:
    cont = cont+1
    termo += razao
    print(termo)

print('FIM!')
