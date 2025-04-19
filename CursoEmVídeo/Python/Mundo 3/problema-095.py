time = []
jogador = {}
partidas = []

while True:
  jogador.clear()
  jogador['NOME'] = str(input('Nome do jogador: '))
  tt_partidas = int(input(f'Quantas partidas que {jogador["NOME"]} jogou: '))
  partidas.clear()
  for c in range(0, tt_partidas):
    partidas.append(int(input(f'  Quantidade de gol(s) na {c+1}º partida: ')))
  jogador['GOL(S)'] = partidas[:]
  jogador['TOTAL'] = sum(partidas)
  time.append(jogador.copy())
  while True:
    res = str(input('Continuar? [S/N]: ')).strip().upper()[0]
    if res in 'SN':
      break
    print('ERRO! Digite [S ou N]', end='')
  if res == 'N':
    break

print('-' * 45)
print('COD    ', end='')
for i in jogador.keys():
  print(f'{i:<15}', end='')
print()
print('-' * 45)
for k, v in enumerate(time):
  print(f'{k:>3} ', end='')
  for d in v.values():
    print(f'{str(d):<15}', end='')
  print()
print('-' * 45)

while True:
  busca = int(input('Motrar DADOS de qual jogador? [999 p/ encerrar]: '))
  if busca == 999:
    break
  if busca >= len(time):
    print(f'ERRO! COD inexistente.')
  else:
    print(f'  - DADOS do jogador {time[busca]["NOME"]}: ')
    for i, g in enumerate(time[busca]["GOL(S)"]):
      print(f'    Na {i + 1}ª partida fez {g} gol(s)')
  print('-' * 45)

#Por Emerson Machado 16/04/2025