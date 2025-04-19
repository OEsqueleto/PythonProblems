aluno = dict()
aluno['nome'] = str(input('Qual é o nome do aluno? ')).strip()
aluno['media'] = float(input(f'Qual é a média de {aluno.get("nome")}? '))

if aluno['media'] >= 6.0:
    print(f'{aluno["nome"]} foi APROVADO!')
else:
    print(f'{aluno["nome"]} foi REPROVADO!')

#Por Emerson Machado 15/04/2025