time = list()

while True:
    print('-'*45)
    jogador = dict()
    gols = list()
    jogador['nome'] = str(input('Nome do Jogador: '))
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    jogador['gols'] = gols
    for p in range(1, jogador['partidas']+1):
        jogador['gols'].append(int(input(f'  Quantos gols na {p}ª partida? ')))
    jogador['total'] = sum(jogador['gols'])
    time.append(jogador.copy())
    c = ''
    while True:
        c = str(input('Quer continuar? [S/N] ')).strip().upper()
        if c in 'SN' and c != '':
            break
        else:
            print('ERRO! Por favor, digite apenas S ou N.')
    if c == 'N':
        break

print('-=-'*17)
print(f'{"cod":>3}', end=' ')
for k in jogador.keys():
    if k == 'total' or k == 'partidas':
        print(f'{k:<8}', end=' ')
    else:
        print(f'{k:<15}', end=' ')
print()
print('-'*51)
for i, j in enumerate(time):
    print(f'{i:>3}', end=' ')
    for v in j.values():
        if str(v).isnumeric():
            print(f'{str(v):<8}', end=' ')
        else:
            print(f'{str(v):<15}', end=' ')
    print()
print('-'*51)

while True:
    dados = int(input('Mostrar dados de qual jogador? [999 encerra] '))
    if dados == 999:
        break
    elif dados >= len(time) or dados < 0:
        print('ERRO! Código de jogador não cadastrado! tente novamente.')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[dados]["nome"]}:')
        for j, g in enumerate(time[dados]['gols']):
            print(f'    No jogo {j+1} fez {g} gols.')
        print(f'  TOTAL: {time[dados]["total"]} gols.')
    print('-'*40)
print('<< VOLTE SEMPRE >>')
