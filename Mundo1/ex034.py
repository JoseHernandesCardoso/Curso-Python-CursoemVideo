salario = float(input('Qual o salário do funcionário: '))

if salario <= 1250:
    aumento = salario + (salario / 100 * 15)
    print(f'O salário do funcionário com reajuste de 15% é de R${aumento:.2f}')
else:
    aumento = salario + (salario / 100 * 10)
    print(f'O salário do funcionário com reajuste de 10% é de R${aumento:.2f}')
