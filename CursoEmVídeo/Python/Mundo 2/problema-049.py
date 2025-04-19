num = float(input('Digite seu número: '))
lim = int(input('Digite seu Limite: '))

for c in range (0,lim+1,1):
    print('      {:.2f} vezes {:.0f} igual a {:.2f}'.format(num,c,num*c))
print('FIM!')
