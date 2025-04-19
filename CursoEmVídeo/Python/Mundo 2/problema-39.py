from datetime import datetime
atual = datetime.today().year
nascimento = int(input('\033[1;36mEm que ano você NASCEU? ')) 

idade = atual - nascimento
if idade == 18:
    print('\033[1;32mTA NA HORA DE ALISTAR!')
elif idade >= 18:
    print('\033[1;31mSEU ALISTAMENTE JÁ PASSOU em {} anos!'.format(idade-18))
else:
    print('\033[1;33mAGUARDE! Daqui a {} anos o ALISTAMENTO MILITAR É OBRIGATÓRIO!'.format(18-idade))
    