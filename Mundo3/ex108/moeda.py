def dobro(n):
    return n * 2


def metade(n):
    return n / 2


def aumentar(n, a):
    return n + (n * (a/100))


def diminuir(n, d):
    return n - (n * (d/100))


def moeda(n):
    formatado = f'R${n:.2f}'.replace('.', ',')
    return formatado