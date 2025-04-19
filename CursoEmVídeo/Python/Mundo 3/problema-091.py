import random
dado = dict()
print('\nVALORES SORTEADOS')

for c in range(1,5):
    dado[f"Jog{c}"] = random.randrange(1,7)
    print(f'Jogador {c} rolou {dado[f"Jog{c}"]}')

print('\nRANKING DOS JOGADORES:')

pos  = 1
for jog, valor in sorted(dado.items(), key=lambda x: x[1],reverse=True):
    print(f'{pos}º Lugar! Vai para {jog} com {valor}!')
    pos += 1

#Por Emerson Machado 15/04/2025