n = int(input('Digite um número para ver seu fatorial: '))
r = n
print(n, end='')
while n != 1:
    n -= 1
    r *= n
    print(f' X {n}', end='')
print(f' = {r}')
