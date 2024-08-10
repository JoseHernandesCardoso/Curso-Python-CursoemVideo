from time import sleep
def linha():
    print('-=-'*15)


def cont(i, f, p):
    if p == 0:
        p = 1
    elif p < 0 and i < f:
        temp = i
        i = f
        f = temp
    linha()
    print(f'contagem de {i} até {f} de {p if p>0 else -p} em {p if p>0 else -p}')
    if i < f:
        f += 1
    elif i > f:
        f -= 1
        if p > 0:
            p = -p
    for num in range(i, f, p):
        print(num, end=' ')
        sleep(0.3)
    print('FIM!')
    linha()


cont(1, 10, 1)
cont(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem!')
cont(
    i = int(input('Início: ')),
    f = int(input('Fim: ')),
    p = int(input('Passo: ')))
