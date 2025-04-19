contador = 0
maior = 0
menor = 9999999999999999999
soma = 0
mais = 0
numero = 0

print('Digite [999] para Parar!')
while True:
        numero = int(input('Digite número: '))
        if numero != 999:
            contador += 1
            maior = max(maior,numero)
            menor = min(menor,numero)
            soma += numero 
            media = soma/contador
        else:
            break


print(f'\nMaior número: {maior}')
print(f'menor número: {menor}')
print(f'Soma números: {soma}')
print(f'Média número: {media}')
print(f'inser número: {contador}')
