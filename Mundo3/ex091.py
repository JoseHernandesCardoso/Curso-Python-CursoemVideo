from random import randint
from time import sleep

jogadores = dict()
jogadores['jogador1'] = randint(1, 6)
jogadores['jogador2'] = randint(1, 6)
jogadores['jogador3'] = randint(1, 6)
jogadores['jogador4'] = randint(1, 6)

print('Valores sorteados:')
for k, v in jogadores.items():
    sleep(1)
    print(f'    O {k} tirou {v}')
sleep(1)

print('Ranking dos jogadores:')
ranking = dict(sorted(jogadores.items(), key=lambda item: item[1], reverse=True))
cont = 1
for k, v in ranking.items():
    sleep(1)
    print(f'    {cont}º lugar: {k} com {v}')
    cont += 1
