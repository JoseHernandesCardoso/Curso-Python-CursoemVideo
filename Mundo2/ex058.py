from random import randint

n = randint(0, 10)
tentativas = 1

print('Vou pensar em um número de 0 a 10!\nEm quantas tentativas você consegue adivinhar o meu número?\n')

palpite = int(input('Qual o seu primeiro palpite: '))
while palpite != n:
    tentativas += 1
    if palpite > n:
        mais_menos = 'Menos'
    elif palpite < n:
        mais_menos = 'Mais'
    palpite = int(input(f'{mais_menos}! Qual o seu {tentativas}º palpite: '))

if tentativas == 1:
    print('VOCÊ ADIVINHOU O NÚMERO DE PRIMEIRA! PARABÉNS!')
else:
    print(f'\nPARABÉNS! Você adivinhou o número em {tentativas} tentativas!')