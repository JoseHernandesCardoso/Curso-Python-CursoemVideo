r1 = float(input('Digite o tamanho da primeira reta: '))
r2 = float(input('Digite o tamanho da segunda reta: '))
r3 = float(input('Digite o tamanho da terceira reta: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    if r1 == r2 == r3:
        tipo = 'EQUILÁTERO'
    elif r1 == r2 or r2 == r3 or r1 == r3:
        tipo = 'ISÓSCELES'
    else:
        tipo = 'ESCALENO'
    print(f'As três retas podem formar um triângulo do tipo {tipo}')
else:
    print('As três retas NÃO são capazes de formar um triângulo')
