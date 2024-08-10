dias = int(input('O carro foi alugado por quantos dias? '))
km = float(input('Quantos quilômetros ele rodou? '))

p = (dias * 60) + (km * 0.15)

print(f'O valor a ser pago é de R${p:.2f}')
