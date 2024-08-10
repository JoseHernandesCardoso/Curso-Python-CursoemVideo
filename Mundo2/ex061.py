termo_atual = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termos = 10
cont = 0

while cont != termos:
    cont += 1
    if cont == termos:
        print(termo_atual)
    else:
        print(termo_atual, end=' -> ')
    termo_atual += razao
