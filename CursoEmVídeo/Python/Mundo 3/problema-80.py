conjunto = []
número = 0

for c in range (0,5):
    número = int(input('Digite um número: '))
    if conjunto == []:
        conjunto.append(número)
    else:  
        for pos, valor in enumerate(conjunto):
            if número < valor:
                conjunto.insert(pos,número)
                break
        else:
            conjunto.append(número)

print(conjunto)
