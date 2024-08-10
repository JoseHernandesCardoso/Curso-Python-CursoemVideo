from random import randint


n = tuple(randint(0, 10) for num in range(1, 6))

print('Os valores sorteados foram: ', end='')
for num in n:
    print(num, end=' ')
print(f'\nO maior valor sorteado foi {max(n)}')
print(f'O menor valor sorteado foi {min(n)}')
