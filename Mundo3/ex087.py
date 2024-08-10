matriz = [[], [], []]
somapar = 0
somacoluna = 0
maiorlinha = 0
for l in range(0, 3):
    for c in range(0, 3):
        num = int(input(f'Digite um valor para a posição [{l},{c}]: '))
        matriz[l].append(num)
        if num % 2 == 0:
            somapar += num
        if c == 2:
            somacoluna += num
        if l == 1 and (maiorlinha == 0 or num > maiorlinha):
            maiorlinha = num

print('-=-' * 15)
for l in matriz:
    for n in l:
        print(f'[{n:^5}]', end='')
    print('')
print('-=-' * 15)
print(f'A soma dos valores pares e {somapar}')
print(f'A soma dos valores da terceira coluna é {somacoluna}')
print(f'O maior valor da segunda linha e {maiorlinha}')
