soma = 0
cont = 0
valor = 0

while valor != 999:
    valor = int(input('Digite um número inteiro (999 para parar): '))
    if valor != 999:
        soma += valor
        cont += 1

print(f'Você digitou {cont} números diferentes e a soma entre eles é {soma}')
