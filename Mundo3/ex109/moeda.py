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