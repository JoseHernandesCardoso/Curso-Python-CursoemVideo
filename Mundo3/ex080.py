lista = list()
while True:
    n = int(input('Digite um número: '))
    if len(lista) == 0:
        lista.append(n)
        print('Adicionado o primeiro item da lista...')

    elif lista[0] > n:
        lista.insert(0, n)
        print('Adicionado ao início da lista...')

    elif lista[-1] < n:
        lista.append(n)
        print('Adicionado ao final da lista...')

    else:
        for p, v in enumerate(lista):
            if v < n < lista[p+1]:
                lista.insert(p+1, n)
                print(f'Adicionado na posição {p+1} da lista...')

    if len(lista) == 5:
        break
print('-=-'*10)
print(f'Os valores digitados em ordem foram {lista}')

