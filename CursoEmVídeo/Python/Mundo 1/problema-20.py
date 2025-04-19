import random
alunos = input('Quais são seus alunos?').split()
random.shuffle(alunos)

print('A ordem dos alunos deve ser: {}'.format(alunos))