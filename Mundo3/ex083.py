ex = str(input('Digite uma expressão: '))
abre = ex.count('(')
fecha = ex.count(')')
if abre == fecha:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
