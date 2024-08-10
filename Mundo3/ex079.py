lista = list()
while True:
    v = ''
    while not v.isnumeric():
        v = input('Digite um número: ')
    if v in lista:
        print('O valor já está na lista!')
    else:
        lista.append(v)
        print('Valor adicionado com sucesso...')

    c = ' '
    while c not in 'SN':
        c = input('Quer continuar? [S/N] ').upper()
    if c == 'N':
        break
print('-=-'*10)
print(f'Os valores digitados em ordem crescente são: {sorted(lista)}')
