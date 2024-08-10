num = []
for v in range(0, 5):
    num.append(int(input(f'Digite um valor para a posição {v}: ')))
print('-=-'*15)
print(f'Você digitou os valores {num}')
print(f'o maior valor digitado foi {max(num)} nas posições ', end='')
for p, n in enumerate(num):
    if n == max(num):
        print(f'{p}...', end=' ')

print(f'\no menor valor digitado foi {min(num)} nas posições ', end='')
for p, n in enumerate(num):
    if n == min(num):
        print(f'{p}...', end=' ')
