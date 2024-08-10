lista = list()
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    c = ' '
    while c not in 'SN':
        c = str(input('Quer continuar? [S/N] ')).strip().upper()
    if c == 'N':
        break
lista.sort(reverse=True)
print('-=-'*10)
print(f'Foram digitados {len(lista)} números')
print(f'Na ordem decrescente, a lista fica {lista}')
if 5 in lista:
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista')
