total = 5
contador = 0
maior = 0
menor = 999999999999999
soma = 0
mais = 1

while mais>= 1:
    while contador != total: 
        numero = int(input('Digite número: '))
        contador += 1
        maior = max(maior,numero)
        menor = min(menor,numero)
        soma += numero 
        media = soma/contador

    while contador == total and mais >= 1:
        mais = int(input('Você quer digitar mais quantos números? '))
        total += mais

print(maior)
print(menor)
print(soma)
print(media)
