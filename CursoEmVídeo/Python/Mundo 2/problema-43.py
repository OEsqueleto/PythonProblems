altura = float(input('\033[0;37mQual a sua altura? '))
peso = float(input('Qual é o seu peso? '))
IMC = peso / altura**2

if IMC <= 18.5:
    print('\033[1;31mMAGREZA! Seu IMC é: {:.2f}'.format(IMC))
elif IMC <= 25:
    print('\033[1;32mIDEAL! Seu IMC é: {:.2f}'.format(IMC))
elif IMC <= 30:
    print('\033[1;33mSOBREPESO! Seu IMC é: {:.2f}'.format(IMC))
elif IMC <= 40:
    print('\033[1;31mOBESIDADE! Seu IMC é: {:.2f}'.format(IMC))
else:
    print('\033[1;31mOBESIDADE MÓRBIDA! Seu IMC é: {:.2f}'.format(IMC))
