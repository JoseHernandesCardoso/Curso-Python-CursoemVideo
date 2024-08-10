speed = int(input('Qua a velocidade do carro (Km/h): '))

if speed > 80:
    multa = (speed - 80)*7
    print(f'O CARRO ULTRAPASSOU O LIMITE DE VELOCIDADE! Ele recebera uma multa de R${multa}!')
else:
    print('O carro está dentro do limite de velocidade.')
