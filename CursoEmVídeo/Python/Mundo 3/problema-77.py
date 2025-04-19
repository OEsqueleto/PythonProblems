produtos = ('Teclado','Mouse','Computador','Monitor','Gabinete','Impressora','Quadro','Porta','Celular','Troféu','Caneta','Papel')
vogal = ('a','e','i','o','u')
vogais_encontradas = tuple((''))

for palavra in produtos:
    vogais_encontradas = tuple((''))
    for letra in palavra:
        if letra.lower() in vogal:
            vogais_encontradas += (letra,)
    print(f'A palavra {palavra} tem {len(vogais_encontradas)} vogais: {", ".join(vogais_encontradas)}')
