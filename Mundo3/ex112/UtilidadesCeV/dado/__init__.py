def leiaDinheiro(txt):
    valido = False
    while True:
        n = input(txt).strip()
        if n.replace('.', '').isdigit() or n.replace(',', '').isdigit():
            if ',' in n:
                n = n.replace(',', '.')
            break
        else:
            print(f'\033[0;31mERRO! "{n}" não é um valor monetário valido!\033[m')

    return float(n)

