
from time import sleep
def titulo(txt):
    tam = len(txt)+2
    print('~'*tam)
    print(f'{txt:^{tam}}')
    print('~'*tam)


def color(cor='none'):
    if cor == 'none':
        style = '\033[m'
    elif cor == 'azul':
        style = '\033[0;34m'
    elif cor == 'ciano':
        style = '\033[0;36m'
    elif cor == 'verde':
        style = '\033[0;32m'
    elif cor == 'vermelho':
        style = '\033[0;31m'
    elif cor == 'back_cinza':
        style = '\033[0;30;47m'
    print(style, end='')


while True:
    color('verde')
    titulo(' SISTEMA DE AJUDA PyHELP ')
    sleep(0.5)
    color('azul')
    r = input('Função ou biblioteca > ').strip()
    if r.lower() in 'fim' and r not in '':
        color('vermelho')
        titulo('ATÉ LOGO')
        sleep(1)
        break
    color('ciano')
    titulo(f'Acessando manual do comando/biblioteca "{r}"')
    sleep(1)
    color('back_cinza')
    help(r)
    sleep(1)
