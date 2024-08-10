media = 0
velho_idade = 0
velho = ''
menos20 = 0
for c in range(1, 5):
    print('-=-'*15)
    nome = input(f'Nome da pessoa {c}ª: ')
    idade = int(input(f'Idade da pessoa {c}ª: '))
    sexo = input(f'Sexo da pessoa {c}ª: (M/F) ').upper()

    if sexo == 'M' and idade > velho_idade:
        velho_idade = idade
        velho = nome
    if sexo == 'F' and idade < 20:
        menos20 += 1
    media += idade
media /= 4

print('-=-'*15)
print(f'''A média de idade do grupo é de {media:.2f};
O homem mais velho do grupo chama-se {velho} e tem {velho_idade} anos;
Há no total {menos20} mulheres menores de 20 anos.''')
