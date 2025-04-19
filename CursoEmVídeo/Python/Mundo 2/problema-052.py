num = int(input('Digite um número: '))
raiz = num**0.5
div = False

for c in range(2,int(raiz)+1):
    if num%c == 0:
        print('O número {} NÃO é PRIMO! pois é divisível por {}'.format(num,c))
        div = True
        break
if not div:
    print('O número {} é PRIMO!'.format(num))
print('FIM')
