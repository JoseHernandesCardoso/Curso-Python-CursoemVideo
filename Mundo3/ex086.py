matriz = [[], [], []]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Digite um valor para a posição [{l},{c}]: ')))

print('-=-'*15)
for l in matriz:
    for n in l:
        print(f'[{n:^5}]', end='')
    print()
