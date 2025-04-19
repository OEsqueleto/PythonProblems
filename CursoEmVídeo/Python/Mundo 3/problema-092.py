from datetime import date
print('Bem Vindo!')
user = dict()
ano = date.today()
atual = ano.year

user["nome"] = str(input('Qual seu nome? ')).strip().capitalize()
user["nascimento"] = int(input(f'Qual sua data de nascimento, {user["nome"]}? '))
user["idade"] = atual - user["nascimento"]
user["carteira"] = int(input(f'Qual a sua carteira de trabalho, {user["nome"]}? Caso não tenha coloque "0" '))

if user["carteira"] != 0:
    user["contribuicao"] = int(input(f'Qual é seu ano de contribuição, {user["nome"]}? '))
    user["salario"] = int(input(f'Qual é o seu salário, {user["nome"]}? R$ '))
    user["aposentadoria"] = 35 - (atual - user["contribuicao"]) 
else:
    print('VAI TRABALHAR VAGABUNDO!')
     
print('\n',user)
print(f'Você vai se aposentar em: {atual+user["aposentadoria"]}. Com {user["idade"]+user["aposentadoria"]} anos!')

#Por Emerson Machado 15/04/2025