frase = input('Digite uma frase: ').upper()
frase = frase.replace(' ', '')
frase_inv = frase[::-1]
print(f'A frase digitada ao contrário é {frase_inv}')
if frase == frase_inv:
    print('E É um palíndromo')
else:
    print('E NÃO É um palíndromo')
