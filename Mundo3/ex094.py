pessoas = list()
while True:
    pessoa = dict()
    pessoa['nome'] = str(input('Nome: '))
    sexo = ''
    while sexo not in 'MF' or sexo == '':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
        if sexo not in 'MF':
            print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['sexo'] = sexo
    pessoa['idade'] = int(input('Idade: '))
    pessoas.append(pessoa)

    c = ''
    while c not in 'SN' or c == '':
        c = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if c not in 'SN':
            print('ERRO! Por favor, digite apenas S ou N.')
    if c == 'N':
        break

print('-=-'*15)
totpes = len(pessoas)
medidade = 0
for p in pessoas:
    medidade += p['idade']
medidade /= totpes

acimamed = list()
for p in pessoas:
    if p['idade'] >= medidade:
        acimamed.append(p.copy())

print(f'- O grupo tem {totpes} pessoas.')
print(f'- A média de idade do grupo é {medidade:.2f} anos.')
print('- As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')
print('\n- As pessoas qe tem idade acima da media são: ')
for p in acimamed:
    print(f'    => {p["nome"]} com {p["idade"]} anos.')
print('<<ENCERRANDO>>')
