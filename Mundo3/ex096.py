def area(larg, comp):
    area = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {area}m2')


print('Controle de Terrenos')
print('-'*20)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)
