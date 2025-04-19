a = float(input('\033[1;37mDigite o tamanho da reta A '))
b = float(input('Digite o tamanho da reta B '))
c = float(input('Digite o tamanho da reta C '))

maior = max(a,b,c)
soma = (a+b+c) - maior
if soma > maior:
    print('\033[1;32mAs retas formam um triângulo! Mas Qual?')
    if a == b and b == c:
        print('EQUILÁTERO: Todos os lados são iguais!')
    elif a != b and b != c and c != a:
        print('ESCALENO: Todos os lados são diferentes!')
    else:
        print('ISÓCELES: Dois lados iguais e um diferente!')
else:
    print('\033[1;31mAs retas não formam um triângulo!')
    