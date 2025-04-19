def escreva(msg):
    comp = len(msg) + 2
    print('~' * comp)
    print(f'{msg.center(comp)}')
    print('~' * comp)
    
msg = str(input('\nDigite sua mensagem! ')).strip()
print(escreva(msg))

#Por Emerson Machado 16/04/2025    