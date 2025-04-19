km_preco = 0.15
dia_preco = 60

km = int(input('Quantos Km rodados?'))
dia = int(input('Quantos dias rodados?'))

pagar = (km_preco * km) + (dia_preco * dia)

print('Com {:.2f}KMs rodados e {} dias rodados, o valor a pagar é {:.2f}'.format(km,dia,pagar))

#Por Emerson Machado 24/03/2025