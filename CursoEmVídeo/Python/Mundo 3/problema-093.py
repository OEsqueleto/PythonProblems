print('Aproveitamento de Jogador por Partida!')
jog = dict()
gols = list()
total = 0

jog["nome"] = str(input('Nome do Jogador: ')).strip().capitalize()
jog["partidas"] = int(input(f'Quantas Partidas, {jog["nome"]} jogou? '))

for c in range(0,jog["partidas"]):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))
    
for g in gols:
    total += g
            
jog["gol"] = gols[:]
print(f'O jogador {jog["nome"]} fez {total} gols em {jog["partidas"]} Partidas!')
for c in range(0,jog["partidas"]):
    print(f'     => {c+1}º Jogo fez {gols[c]} gols.')
print(f'=> No total fez {total} gols!')

#Por Emerson Machado 15/04/2025    