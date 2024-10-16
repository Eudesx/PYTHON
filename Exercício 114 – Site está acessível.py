import ssl
import urllib.request

# Ignora a validação SSL
context = ssl._create_unverified_context()

try:
    site = urllib.request.urlopen('https://www.pudim.com.br', context=context)
except urllib.error.URLError:
    print('Deu, ERRO!')
else:
    print('Todo OK')
    print(site.read())

