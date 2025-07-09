import urllib
import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site pudim nao esta disponivel no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso.')
    # print(site.read())