import csv
#Dados que serão escritos:
dados = [
    ['Item','Quantity'],
    ['Blender',2],
    ['Posters',30],
    ['Shoes',2]
]
#Tenta ler packing.csv, se encontrar imprime todas as linhas
try:
    with open(r'C:\Users\PC-XEON\Documents\EMERSON\packing.csv', 'r') as file:
        csv_leitor = csv.reader(file)
        for c in csv_leitor:
            print(c)
#Se não encontrado, avisa, e cria novo arquivo packing.csv            
except FileNotFoundError:
    print('Packing List NOT found! Creating a new one...')
    with open(r'C:\Users\PC-XEON\Documents\EMERSON\packing.csv', 'w', newline='') as file:
        csv_escriba = csv.writer(file)
        csv_escriba.writerows(dados)
#By Emerson!