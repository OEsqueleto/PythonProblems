import datetime

def voto(ano):
    if datetime.date.today().year - ano >= 65:
        return f'Com {datetime.date.today().year - ano} anos o Voto é OPICIONAL'
    elif datetime.date.today().year - ano >= 18:
        return f'Com {datetime.date.today().year - ano} anos o Voto é OBRIGATÓRIO'
    elif datetime.date.today().year - ano < 18:
        return f'Com {datetime.date.today().year - ano} anos o Voto é PROÍBIDO'

ano = int(input('\nEm que ano você nasceu? '))
print(voto(ano))
#Por Emerson Machado 16/04/2025