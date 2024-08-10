def fatorial(num, show=False):
    """
    --> Calcula o fatorial de um número?
    :param num: O valor a ser calculado
    :param show: Mostra a conta (PADRÃO = FALSE)
    :return: Retorna o fatorial de num
    """
    fat = 1
    for n in range(num, 1, -1):
        fat *= n
        if show:
            print(n, end=' X ')
    if show:
        print(f'1 = ', end='')
    return fat


print(fatorial(5, show=True))
help(fatorial)
