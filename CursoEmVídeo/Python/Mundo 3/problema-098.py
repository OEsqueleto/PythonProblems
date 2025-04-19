from time import sleep
def loop(i,f,p):
    p = abs(p)
    if p == 0: p = 1
    if i < f:
        while i < f:
                print(i,end=' ',flush=True)
                i += p 
                sleep(0.2)
    else:
        while i > f:
                print(i,end=' ',flush=True)
                i -= p
                sleep(0.2)
    if i == f:
        print(i)
        print('FIM!\n')
        
loop(1,10,1)
loop(10,0,2)

print('Agora é a sua vez de usar o LOOP!')
ini = int(input('Inicio: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))

loop(ini,fim,pas)

#Por Emerson Machado 16/04/2025