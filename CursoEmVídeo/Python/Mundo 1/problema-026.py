frase = input('Digite uma frase:').strip()
letra = 'a'
lista = frase.split()
print('Na sua Frase "{}" apareceu {} quantas vezes? Apareceu {} vezes'.format(frase,letra,frase.lower().count(letra)))
print('Apareceu pela primeira vezes em {}, e por último em {}'.format(frase.lower().find(letra)+1,frase.lower().rfind(letra)+1))
