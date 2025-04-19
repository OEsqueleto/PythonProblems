print('TABELA DO BRASILEIRÃO 2025')
tabela = ('Fortaleza','Juventude','Vasco da Gama','Cruzeiro','Grêmio','Bragantino','Ceará SC','Corinthias','Flamengo','Internacional',
          'Bahia','São Paulo','Sport Recife','Botafogo','Palmeiras','Atlético MG','Santos','Mirassol','Fluminense','EC Vitória')

print(tabela)
print('TOP 5')
print(tabela[0:5])
print('ÚLTIMOS 4')
print(tabela[-4:])
print('ALFABÉTICA:')
print(sorted(tabela))
print(f'{tabela[7]} está em {tabela.index("Corinthias")+1}º Lugar')
