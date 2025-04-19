import random

numeros = list(range(1,61))
print('\n','JOGO DA MEGA-SENA!','\n')

jogos = int(input('Quer sortear quantos jogos? '))
print('-'*40)
print(f'Sorteando {jogos} Jogos!')

for c in range (1,jogos+1):
    print(f'Jogo {c}º: {random.sample(numeros, k=6)}')  
print('\n','BOA SORTE BOBÃO!')
