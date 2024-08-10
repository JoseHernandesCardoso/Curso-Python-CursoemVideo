def dobro(n, formatado=False):
    valor = n * 2
    if formatado:
        return moeda(valor)
    else:
        return valor


def metade(n, formatado=False):
    valor =  n / 2
    if formatado:
        return moeda(valor)
    else:
        return valor


def aumentar(n, a, formatado=False):
    valor = n + (n * (a/100))
    if formatado:
        return moeda(valor)
    else:
        return valor


def diminuir(n, d, formatado=False):
    valor = n - (n * (d/100))
    if formatado:
        return moeda(valor)
    else:
        return valor


def moeda(n):
    formatado = f'R${n:.2f}'.replace('.', ',')
    return formatado


def resumo(n, a, d):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print(f'{"Preço analisado:":<20}{moeda(n)}')
    print(f'{"Dobro do preço:":<20}{dobro(n, True)}')
    print(f'{"Metade do preço:":<20}{metade(n, True)}')
    print(f'{f"{a}% de aumento:":<20}{aumentar(n, a, True)}')
    print(f'{f"{d}% de redução:":<20}{diminuir(n, d, True)}')
    print('-'*30)
