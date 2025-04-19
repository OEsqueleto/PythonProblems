from uteis import moeda_03

p = float(input('Preço da moeda: R$ '))
print(f'A metade de {moeda_03.dinheiro(p)} é {moeda_03.metade(p)}!')
print(f'O dobro de {moeda_03.dinheiro(p)} é {moeda_03.dobro(p,f=True)}!')
print(f'Aumentando em 10%. Temos {moeda_03.aumentar(p, 10)}!')
print(f'Diminuindo em 13%. Temos {moeda_03.diminuir(p, 13,f=True)}!')
#Por Emerson Machado 18/04/2025