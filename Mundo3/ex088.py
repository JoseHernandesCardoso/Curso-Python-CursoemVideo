from time import sleep
from random import randint

print('-'*30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-'*30)
tot = int(input('Quantos jogos você quer que eu sorteie? '))

sorteios = []
for j in range(1, tot+1):
    jogo = []
    for n in range(0, 6):
        while True:
            num = randint(1, 60)
            if num not in jogo:
                jogo.append(num)
                break
    jogo.sort()
    sorteios.append(jogo[:])

print(f'-=-=-= SORTEANDO {tot} JOGOS -=-=-=')
for i, j in enumerate(sorteios):
    sleep(1)
    print(f'Jogo {i+1}: {j}')
print('-=-=-=-= < BOA SORTE! > -=-=-=-=')
