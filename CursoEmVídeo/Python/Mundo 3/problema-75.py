conjunto =  (int(input('Digite valor até 10: ')),int(input('Digite valor até 10: ')), 
             int(input('Digite valor até 10: ')),int(input('Digite valor até 10: ')))

print(f'Você digitou o conjunto:{conjunto}')
pares = ()

for numeros in conjunto:
    if numeros %2 == 0:
        pares += (numeros,)

print(f'\nOs números pares são: {pares}')
print(f'O valor 9 apareceu {conjunto.count(9)} vez!')
print(f'O número 3 apareceu primeiro na posição: {conjunto.index(3)+1}º')
