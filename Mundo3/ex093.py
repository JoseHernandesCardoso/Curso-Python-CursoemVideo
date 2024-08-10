jogador = dict()
gols = list()
jogador['nome'] = str(input('Nome do Jogador: '))
jogador['jogos'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
jogador['gols'] = gols[:]
for p in range(1, jogador['jogos']+1):
    jogador['gols'].append(int(input(f'Quantos gols na {p}ª partida? ')))
jogador['total'] = sum(jogador['gols'])

print('-=-'*15)

print(f'O jogador {jogador["nome"]} jogou {jogador["jogos"]} partidas.')
for p, v in enumerate(jogador['gols']):
    print(f'    => Na partida {p+1}, fez {v} gols.')
print(f'foi um total de {jogador["total"]} gols.')
