import requests

try:
    requests.get('https://www.pudim.com.br')
except:
    print('\033[0;31mO site pudim.com.br não está disponível no momento! :(\033[m')
else:
    print('\033[0;32mO site do pudim está disponível! :D \033[m')
