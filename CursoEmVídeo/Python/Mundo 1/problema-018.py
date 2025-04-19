import math
ang = int(input('Angulo: '))
rad = math.radians(ang)
sen = math.sin(rad)
con = math.cos(rad)
tan = math.tan(rad)

print('Esse são o {:.2f} Seno, o {:.2f} Cosseno e a {:.2f} tangente'.format(sen,con,tan))