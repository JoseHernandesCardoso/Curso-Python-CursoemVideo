def estilo(estilo='none', cor='none', fundo='none'):
    #estilo da fonte
    if estilo == 'negrito':
        cod_estilo = '1'
    elif estilo == 'fraco':
        cod_estilo = '2'
    elif estilo == 'italico':
        cod_estilo = '3'
    elif estilo == 'underline':
        cod_estilo = '4'
    elif estilo == 'inverter':
        cod_estilo = '7'
    else:
        cod_estilo = '0'

    #cores da fonte
    if cor == 'preto':
        cod_cor = '30'
    elif cor == 'vermelho':
        cod_cor = '31'
    elif cor == 'verde':
        cod_cor = '32'
    elif cor == 'amarelo':
        cod_cor = '33'
    elif cor == 'azul':
        cod_cor = '34'
    elif cor == 'magenta':
        cod_cor = '35'
    elif cor == 'ciano':
        cod_cor = '36'
    elif cor == 'cinza':
        cod_cor = '37'
    else:
        cod_cor = '38'

    #background da fonte
    if fundo == 'preto':
        cod_fundo = '40'
    elif fundo == 'vermelho':
        cod_fundo = '41'
    elif fundo == 'verde':
        cod_fundo = '42'
    elif fundo == 'amarelo':
        cod_fundo = '43'
    elif fundo == 'azul':
        cod_fundo = '44'
    elif fundo == 'magenta':
        cod_fundo = '45'
    elif fundo == 'ciano':
        cod_fundo = '46'
    elif fundo == 'cinza':
        cod_fundo = '47'
    else:
        cod_fundo = '48'

    print(f'\033[{cod_estilo};{cod_cor};{cod_fundo}m', end='') #aplicando estilo
