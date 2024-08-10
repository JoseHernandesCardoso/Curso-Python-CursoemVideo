peso = float(input('Digite seu peso (Kg): '))
altura = float(input('Digite sua altura (m): '))
imc = peso / altura ** 2

if imc < 18.5:
    status = 'ABAIXO DO PESO'
elif imc < 25:
    status = 'PESO IDEAL'
elif imc < 30:
    status = 'SOBREPESO'
elif imc < 40:
    status = 'OBESIDADE'
else:
    status = 'OBESIDADE MÓRBIDA'

print(f'Você tem um IMC de {imc:.2f} e está em {status}')
