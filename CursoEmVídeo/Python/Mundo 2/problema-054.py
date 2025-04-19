from datetime import date
aniversario = []
ano = date.today().year
for c in range (7):
    data = int(input('Ano de nascimento da {}° Pessoa: '.format(c+1)))
    aniversario.append({ 'nascimento':data })

print(aniversario)

for pessoa in aniversario:
        if  ano -  pessoa['nascimento'] >= 18:
            print('Essa pessoa é MAIOR de idade! Tem {} anos!'.format(ano - pessoa['nascimento']))
        else:
            print('Essa pessoa é MENOR de idade! Tem {} anos!'.format(ano - pessoa['nascimento']))
