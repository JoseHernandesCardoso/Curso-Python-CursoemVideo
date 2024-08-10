cont = maior = menor = soma = 0
continuar = 'S'
while continuar == 'S':
    n = int(input('Digite um valor: '))

    if cont == 0:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    soma += n
    cont += 1
    continuar = input('Você quer continuar [S/N]: ').upper().strip()[0]
    while continuar not in ['S', 'N']:
        continuar = input('RESPOSTA INVÁLIDA! Você quer continuar [S/N]: ').upper().strip()[0]

print(f'\nVocê digitou um total de {cont} números\nA média entre eles foi {soma/cont}\nO menor e maior valor foram {menor} e {maior}')
