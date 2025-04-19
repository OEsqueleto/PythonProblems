array = [[],[],[]]
maior = pares = soma = 0
for linha in range (0,3):
    for coluna in range (0,3):
        user = int(input(f'Digite um valor na posição [{linha},{coluna}]: '))
        array[linha].append(user)
        if linha == 1 and user > maior:
            maior = user
        if coluna == 2:
            soma += user
        if user % 2 == 0:
            pares += user
print('-'*40)     
for linha in range(0,3):
    print()
    for coluna in range (0,3):   
        print(f' [ {array[linha][coluna]:^5} ] ',end='')    
print('\n','-'*40)
print(f'Soma dos valores pares: {pares}')
print(f'Soma dos valores da 3º Coluna: {soma}')
print(f'Soma dos valores da 2 Linha: {maior}')
