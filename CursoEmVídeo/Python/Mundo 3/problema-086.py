array = [[],[],[]]

for linha in range (0,3):
    for coluna in range (0,3):
        array[linha].append(int(input(f'Digite um valor na posição [{linha},{coluna}]: ')))

print('-'*40)     
for linha in range(0,3):
    print()
    for coluna in range (0,3):   
        print(f' [ {array[linha][coluna]:^5} ] ',end='')    