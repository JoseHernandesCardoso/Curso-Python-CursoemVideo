s = 0
for c in range(3, 501, 3):
    if c % 2 != 0:
        s += c
print(f'A soma de todos os números impares múltiplos de 3 entre 1 e 500 é de {s}')
