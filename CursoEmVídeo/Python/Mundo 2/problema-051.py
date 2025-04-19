termo = int(input('Qual o primeiro termo? '))
razao = int(input('Qual a RAZÃO? '))
total = int(input('Quantos termos deseja ver? '))

for c in range (termo,termo+(total)*razao,razao):
    print(c)
print('FIM')
