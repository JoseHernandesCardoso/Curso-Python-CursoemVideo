registro = list()
while True:
    aluno = list()
    notas = list()
    aluno.append(str(input('Nome: ')))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    aluno.append((notas[0] + notas[1]) / 2)
    aluno.append(notas[:])
    registro.append(aluno[:])

    c = ' '
    while c not in 'SN':
        c = str(input('Quer continuar? [S/N] ')).strip().upper()
    if c == 'N':
        break

print('-=-'*20)

print(f'{"No.":<4}{"NOME":<16}{"MÉDIA":<5}')
print('-'*25)
for i, a in enumerate(registro):
    print(f'{i:<4}{a[0]:<17}{a[1]:<5.1f}')

print('-'*25)

while True:
    id = int(input('Mostrar as notas de qual aluno? (999 interrompe): '))
    if id == 999:
        break
    elif id <= len(registro)-1:
        print(f'As notas de {registro[id][0]} são {registro[id][2]}')
        print('-'*50)

print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
