import random
print('\033[1;37m='*10 + '\033[1;36m PEDRA PAPEL TESOURA ' + '\033[1;37m='*10)

user = str(input('Escolha entre: Pedra, Papel e Tesoura ')).strip().upper()
computer = random.choice(['PEDRA','PAPEL','TESOURA'])

if user == computer:
    print('\033[1;33mEMPATE! Pois bot {} você {}'.format(computer,user))
elif user == 'PEDRA' and computer == 'TESOURA':
    print('\033[1;32mVITÓRIA! Pois bot {} você {}'.format(computer,user))
elif user == 'PAPEL' and computer == 'PEDRA':
    print('\033[1;32mVITÓRIA! Pois bot {} você {}'.format(computer,user))
elif user == 'TESOURA' and computer == 'PAPEL':
    print('\033[1;32mVITÓRIA! Pois bot {} você {}'.format(computer,user))
else:
    print('\033[1;31mDERROTA! Pois bot {} você {}'.format(computer,user))