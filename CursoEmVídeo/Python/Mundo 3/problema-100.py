import random
números = [1,2,3,4,5,6,7,8,9,10]
print('\nBIEN VENIDO!')

def sorteio(núm):
    sorte = random.choices(núm, k=5)
    print(f'Sorteando 5 valores da Lista! {sorte}')

def somapar(núm):
    tot = 0
    pares = [n for n in núm if n % 2 == 0]
    for n in pares: tot += n
    print(f'Números pares sorteados: {pares}')
    print(f'Soma dos números pares é igual a {tot}')

números_sorteados = sorteio(números)
somapar(números_sorteados)

#Por Emerson Machado 16/04/2025
