n = int(input('Digite um número: '))
print(f'Aqui estão os {n} primeiros números da sequência de fibonacci')
cont = 0
a = 0
c = b = 1
while cont != n:
    if cont != n-1:
        print(a, end=' -> ')
    else:
        print(a)
    a = b
    b = c
    c = a + b
    cont += 1
