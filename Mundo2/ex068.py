from random import randint

vitorias = 0
print('=-'*12)
print('VAMOS JOGAR PAR OU ÍMPAR')

while True:
    print('=-'*12)
    escolha = ''
    jogador = int(input('Diga um valor de 0 a 10: '))
    computador = randint(0, 10)
    soma = jogador + computador
    while escolha not in ['P', 'I']:
        escolha = input('Par ou Impar? [P/I] ').upper().strip()[0]

    if soma % 2 == 0:
        resultado = 'P'
    else:
        resultado = 'I'

    print('='*24)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU {"PAR" if resultado == "P" else "ÍMPAR"}')
    print('='*24)
    if escolha == resultado:
        vitorias += 1
        print('Você VENCEU!')
        print('Vamos jogar de novo...')
    else:
        print('Você PERDEU!')
        break

print(f'GAME OVER! Você venceu {vitorias} vezes')
