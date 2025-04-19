import requests

def siteonline(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            print(f'\033[1;32mO SITE {url} ESTÁ NO AR!\033[m')
        else:
            print(f'\033[1;31mO SITE {url} RESPONDEU COM: {resposta.status_code}\033[m')
    except requests.exceptions.RequestException as error:
        print(f'\033[1;31mErro ao acessar {url}.ERRO: {error}\033[m')

siteonline('https://www.pudim.com.br/')

#Por Emerson Machado 18/04/2025