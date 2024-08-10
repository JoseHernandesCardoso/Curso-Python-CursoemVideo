pri_ter = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
ult_ter = pri_ter + 10 * r
print('Progressão aritmética: ')
for n in range(pri_ter, ult_ter, r):
    print(n, end=' -> ')
print('FIM')
