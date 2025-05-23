import csv
mais_vendas = 0
info = []

#Abre o arquivo, está codificado como UTF-8
with open(r'C:\Users\PC-XEON\Documents\EMERSON\Bestseller.csv', 'r', encoding='utf-8') as arquivo:
    csv_leitor = csv.reader(arquivo)
#Enumero cada linha, e pulo o cabeçalho
    for i,linha in enumerate(csv_leitor):
        if i != 0: 
            num = float(linha[4]) #Transforma o núm string em float 199.99
            if num > mais_vendas:
                mais_vendas = num
                info = linha
print(info)
#Escreve um novo arquivo, com as informações do livro mais vendido
with open(r'C:\Users\PC-XEON\Documents\EMERSON\SellerInfo.csv', 'w', newline="") as doc:
    csv_escreve = csv.writer(doc)
    csv_escreve.writerow(info)
#By Emerson
