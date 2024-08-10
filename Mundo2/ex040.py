n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
média = (n1 + n2) / 2
if média < 5:
    print('O aluno está REPROVADO!')
elif média < 7:
    print('O aluno está DE RECUPERAÇÃO!')
else:
    print('O aluno está APROVADO!')
print(f'A média do aluno foi de {média:.1f}')