lista = []
c = 0

while True:
    nome = str(input('Nome: ')).strip().lower()
    nota1 = float(input('1º Nota: '))
    nota2 = float(input('2º Nota: '))
    media = (nota1 + nota2) / 2
    lista.append([nome,media,[nota1,nota2]])            
    c += 1
    resposta = str(input('Deseja continuar? [S/N] ')).strip().lower()
    while resposta not in 'sn':
        resposta = str(input(f'Digitaste {resposta}. Queria dizer [S/N]? ')).strip().lower()
    if resposta == 'n':
        break
    
print (lista)    
print('\n','-'*40)
print(f'{"Nº":<4}{"NOME:":^10}{"MÉDIA":>5}')
for i, aluno in enumerate(lista):
    print(f'{i:<4}{aluno[0]:^10}{aluno[1]:>5}')
print('-'*40)
        
while True:
    answer = int(input('Deseja ver notas de quais alunos? (999 PARA) '))
    if answer == 999:
        break
    if answer <= len(lista) -1:
        print(f'Notas de {lista[answer][0]} São de {lista[answer][2]}')
print('FIM!')       