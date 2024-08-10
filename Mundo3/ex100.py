from random import randint
from time import sleep

def Sorteia(list):
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        sleep(0.3)
        num = randint(1, 10)
        list.append(num)
        print(num, end=' ')
    print('PRONTO!')
    sleep(0.5)


def SomaPar(list):
    print(f'Somando os valores pares de {list}, temos ', end='')
    sleep(1)
    pares = 0
    for v in list:
        if v % 2 == 0:
            pares += v
    print(pares)

numeros = []
Sorteia(numeros)
SomaPar(numeros)