r1 = float(input('Segmento da RETA UM: '))
r2 = float(input('Segmento da RETA DOIS: '))
r3 = float(input('Segmento da RETA TRÊS: '))

maior = max (r1,r2,r3)
menores = r1+r2+r3 - maior

if menores >= maior:
    print('SIM, estas retas formam um triângulo')
else: 
    print('NÃO, estas retas não formam um triângulo')
