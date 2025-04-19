termo = int(input('Termo: '))
razao = int(input('Razão: '))
total = int(input('Total: '))
cont = 0
mais = 1

while mais >= 1:
    while cont != total:
        print(termo)
        cont = cont+1
        termo += razao


    while cont == total and mais >= 1:
        mais = int(input('Você quer ver mais quantos termos? '))
        total += mais

print('FIM!')
