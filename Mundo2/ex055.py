for c in range(1, 5):
    peso = float(input(f'Digite o peso da {c}ª pessoa: '))
    if c == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso digitado foi {maior}Kg\nO menor foi {menor}Kg')
