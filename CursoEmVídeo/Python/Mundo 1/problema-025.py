name = input('Qual o seu Nome? ').strip()
key = 'Silva'
have = key.lower() in name.lower()
print('O nome {}, contém o nome {}? {}'.format(name,key.strip(),have))
