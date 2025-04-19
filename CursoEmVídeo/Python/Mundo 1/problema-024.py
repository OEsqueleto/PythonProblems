city = input('Nome da cidade:').strip().split()
key = 'São'
aparece = key.lower() in city[0].lower()
print('A cidade {} começa com {}? {}'.format(' '.join(city),key,aparece))
  