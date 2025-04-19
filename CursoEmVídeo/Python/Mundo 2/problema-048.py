soma = 0
for num in range (1,501,2):
    if num%3 == 0:
        print(num)   
        soma += num
print('SOMÁTORIO: {}'.format(soma))
print('FIM')
