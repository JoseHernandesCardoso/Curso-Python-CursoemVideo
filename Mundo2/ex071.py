print('='*30)
print(f'{"BANCO CEV":^30}')
print('='*30)
valor = int(input('Que valor você quer sacar? R$'))
while True:
    if valor >= 50:
        tipo = 50
    elif valor >= 20:
        tipo = 20
    elif valor >= 10:
        tipo = 10
    elif valor > 0:
        tipo = 1
    else:
        break
    cedulas = valor // tipo
    valor %= tipo
    print(f'Total de {cedulas} cédulas de R${tipo}')
print('='*30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
