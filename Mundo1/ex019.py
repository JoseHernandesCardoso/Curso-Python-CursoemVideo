from random import randint

a1 = input('Aluno 1: ')
a2 = input('aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')
alunos = [a1, a2, a3, a4]

sorteado = randint(0, 3)

print(f'O aluno sorteado para apagar o quadro foi {alunos[sorteado]}')
