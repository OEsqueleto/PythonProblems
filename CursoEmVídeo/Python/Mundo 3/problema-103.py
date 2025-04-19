def ficha(n,g):
    if not n:
        n = '<Desconhecido>'
    if not g:
        g = 0    
    print(f'Jogador {n} fez {g} gols no Campeonato!')

nome = str(input('Nome do Jogador: '))
gols = input('Gols do Campeonato: ')

ficha(nome,gols)

#Por Emerson Machado 16/04/2025