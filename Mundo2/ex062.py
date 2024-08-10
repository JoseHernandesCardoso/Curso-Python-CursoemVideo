termo_atual = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termos = 10
cont = 0
continua = ''

while continua != 0:
    while cont != termos:
        cont += 1
        if cont == termos:
            print(termo_atual)
        else:
            print(termo_atual, end=' -> ')
        termo_atual += razao

    continua = int(input('Quantos termos você gostaria de ver a mais? '))
    if continua != 0:
        termos += continua

print(f'A progressão foi finalizada com {cont} termos mostrados')
