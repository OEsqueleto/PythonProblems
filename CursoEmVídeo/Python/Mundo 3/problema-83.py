expressão = str(input('Sua Expressão com Parênteses: '))
abertos = expressão.count('(')
fechados = expressão.count(')')
esquerda =[]
direita = []

for c, letra in enumerate(expressão):
    if letra == '(':
        esquerda.append(c)
    elif letra == ')':
        direita.append(c)

if abertos == fechados:
    print(f'\nVocê tem {abertos} Abertos e {fechados} Fechados! Quantidade CORRETA')
    for i, (e, d) in enumerate(zip(esquerda,direita), start=1):
        if e > d:
            print(f'ERRO: {i}º Caso: Você tentou FECHAR um parêntese antes de ABRIR')
            break
        else:
            print(f'{i}° Caso: Posicionamento OK')
else:
    print(f'ERRO: Você tem {abertos} Abertos e {fechados} Fechados! Quantidade INCORRETA')
