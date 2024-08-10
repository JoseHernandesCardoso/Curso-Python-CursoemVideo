DeMaior = HTotal = Menor20 = 0
while True:
    sexo = continuar = ''
    print('-'*30)
    print(f'{"CADASTRE UMA PESSOA":^30}')
    print('-'*30)

    idade = int(input('Idade: '))
    while sexo not in ['M', 'F']:
        sexo = input('Sexo: [M/F] ').strip().upper()[0]
    print('-'*30)

    if idade >= 18:
        DeMaior += 1
    if sexo == 'M':
        HTotal += 1
    if idade < 20 and sexo == 'F':
        Menor20 += 1

    while continuar not in ['S', 'N']:
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break

print(f'{"FIM DO PROGRAMA":=^30}')
print(f'O total de homens com mais de 18: {DeMaior}')
print(f'Ao todo temos {HTotal} homens cadastrados')
print(f'E temos {Menor20} mulheres com menos de 20 anos')
