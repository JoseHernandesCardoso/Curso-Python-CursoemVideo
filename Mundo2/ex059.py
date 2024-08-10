n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
opc = 0

while opc != 5:
    print('=-='*12)
    print('''[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA''')
    opc = int(input('Escolha uma opção acima: '))
    print('=-='*12)

    if opc == 1:
        print(f'A soma entre {n1} e {n2} é {n1+n2}')
    elif opc == 2:
        print(f'O resultado da multiplicação de {n1} e {n2} é {n1*n2}')
    elif opc == 3:
        if n1 > n2:
            print(f'O maior valor digitado foi {n1}')
        elif n2 > n1:
            print(f'O maior valor digitado foi {n2}')
        else:
            print('Não há valor maior. Ambos os números são iguais')
    elif opc == 4:
        n1 = int(input('Digite o novo primeiro número: '))
        n2 = int(input('Digite o novo segundo número: '))
    elif opc == 5:
        print('finalizando programa...')
    else:
        print('OPÇÃO INVÁLIDA!')
