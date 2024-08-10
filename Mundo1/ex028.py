from random import randint

escolhido = randint(0, 5)
print('\033[33mEscolhi um número de 0 a 5\033[m')
num = int(input('\033[36mQual número você acha que eu escolhi?\033[m '))

print('-=-'*15)

if num == escolhido:
    print(f'\033[32mPARABÉNS! Você acertou o número!\nO número escolhido era {escolhido}\033[m.')
else:
    print(f'\033[31mQue pena, você ERROU!\nO número escolhido era {escolhido}.\033[m')
