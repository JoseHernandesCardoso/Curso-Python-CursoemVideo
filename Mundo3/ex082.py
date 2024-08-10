lista = list()
while True:
    lista.append(int(input('Digite um número: ')))
    c = ' '
    while c not in 'SN':
        c = str(input('Quer Continuar? [S/N] ')).strip().upper()
    if c == 'N':
        break
par = list()
impar = list()
for v in lista:
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print('-=-'*15)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')
