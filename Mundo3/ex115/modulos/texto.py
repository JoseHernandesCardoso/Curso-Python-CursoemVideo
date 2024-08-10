def linha(tam=45): #cria uma linha com - do tamanho da variável tam
    print('-'*tam)


def titulo(txt='', tam=45): #cria um título com a variável txt do tamanho de tam
    linha(tam)
    print(f'{txt:^{tam}}')
    linha(tam)


def erro(txt):
    print(f'\033[31m{txt}\033[m')