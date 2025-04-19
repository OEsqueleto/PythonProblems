from uteis import moeda

p = float(input('Preço da moeda: R$ '))
print(f'A metade de R${p} é R${moeda.metade(p):.2f}!')
print(f'O dobro de R${p} é R${moeda.dobro(p):.2f}!')
print(f'Aumentando em 10%. Temos R${moeda.aumentar(p, 10):.2f}!')
print(f'Diminuindo em 13%. Temos R${moeda.diminuir(p, 13):.2f}!')
#Por Emerson Machado 17/04/2025