def fatorial(num,show=False):
    """
    fatorial(num, show=False)
    Função que calcula o Fatorial de N número:
    num    -> O número a ser cálculado
    show=  -> Se deseja ver a explicação do cálculo
    return -> O resultado da operação
    """   
    resultado = 1
    for c in range(num,0,-1):
        resultado *= c  
        if show == True:
            print(f'{c}',end=' x ') if c != 1 else print(f'{c}', end= ' = ')
    print(resultado)
print()
fatorial(5,show=True)
help(fatorial)
#Por Emerson Machado 16/04/2025