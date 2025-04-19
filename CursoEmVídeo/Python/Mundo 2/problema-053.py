original = str(input('Digite sua frase: ')).strip()
frase = original.strip().lower().replace(' ','')
invertido = ''.join(reversed(frase))

if invertido == frase:
    print('Sua frase: {} é um PALÍNDROMO!\nSua frase ao contrário {}'.format(original,invertido))
else:
    print('Sua frase: {}  NÃO é um PALÍNDROMO!\nSua frase ao contrário {}'.format(original,invertido))
print('FIM!')
