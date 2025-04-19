import random
um = input('Primeiro aluno: ')
dois = input('Segundo aluno: ')
tres = input('Terceiro aluno: ')
quarto = input('Quarto aluno: ')
alunos = [um,dois,tres,quarto]
escolha = random.choice([um,dois,tres,quarto])

print('O aluno escolhido foi o {}'.format(escolha))
