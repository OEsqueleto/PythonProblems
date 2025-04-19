from datetime import datetime
print('\033[7;37m CONFEDERAÇÃO NACIONAL de NATAÇÃO')
nasci = int(input('\033[0;372mEm que ano você nasceu? '))
atual = datetime.today().year
idade = atual - nasci

if idade <= 9:
    print('\033[1;32mMIRIM! Sua categoria é a Mirim por ter {} anos'.format(idade))
elif idade <= 14:
    print('\033[1;32mINFANTIL! Sua categoria é a Infantil por ter {} anos'.format(idade))
elif idade <= 19:
    print('\033[1;32mJUNIOR! Sua categoria é a Junior por ter {} anos'.format(idade))
elif idade <= 40:
    print('\033[1;32mSÊNIOR! Sua categoria é a Sênior por ter  {} anos'.format(idade))
else: 
    print('\033[1;32mMASTER! Sua categoria é a Master por ter {} anos'.format(idade))
