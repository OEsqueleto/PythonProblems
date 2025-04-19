tupla = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez',
         'Onze','Doze','Treze','Quatorze', 'Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')

user = int(input('Bem vindo! Digite um número de 0 a 20: '))

while True:
    while user in range (0,21):
        print(f'Você digitou o número {tupla[user]}')
        user = int(input('Digite número de 0 a 20: '))
    else:
       user = int(input(f'Você digitou "{user}". Digite número de 0 a 20: '))
