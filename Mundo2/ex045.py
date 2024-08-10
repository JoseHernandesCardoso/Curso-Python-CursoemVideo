from random import randint
from time import sleep

print('-=-'*10)
print(f'{"JOKENPÔ":^30}')
print('-=-'*10)
sleep(1)

print('''Opções:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
jogador = int(input('Qual a sua opção: '))
computador = randint(1, 3)
print('-=-'*10)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

if jogador == 1:
    jogador_opc = 'PEDRA'
elif jogador == 2:
    jogador_opc = 'PAPEL'
elif jogador == 3:
    jogador_opc = 'TESOURA'

if computador == 1:
    computador_opc = 'PEDRA'
elif computador == 2:
    computador_opc = 'PAPEL'
elif computador == 3:
    computador_opc = 'TESOURA'

print('-=-' * 10)
print(f'O jogador jogou {jogador_opc}')
print(f'O computador jogou {computador_opc}')
print('-=-' * 10)

vitoria = 'PARABÉNS! Você VENCEU!'
empate = 'EMPATE! Ambos jogaram a mesma coisa'
derrota = 'Você PERDEU!'

if jogador == computador:
    print(empate)
elif jogador == 1:
    if computador == 2:
        print(derrota)
    elif computador == 3:
        print(vitoria)
elif jogador == 2:
    if computador == 1:
        print(vitoria)
    elif computador == 3:
        print(derrota)
elif jogador == 3:
    if computador == 1:
        print(derrota)
    elif computador == 2:
        print(vitoria)
