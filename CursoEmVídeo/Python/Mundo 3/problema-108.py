from uteis import moeda_02

p = float(input('Preço da moeda: R$ '))
print(f'A metade de {moeda_02.dinheiro(p)} é {moeda_02.metade(p)}!')
print(f'O dobro de {moeda_02.dinheiro(p)} é {moeda_02.dobro(p)}!')
print(f'Aumentando em 10%. Temos {moeda_02.aumentar(p, 10)}!')
print(f'Diminuindo em 13%. Temos {moeda_02.diminuir(p, 13)}!')
#Por Emerson Machado 18/04/2025