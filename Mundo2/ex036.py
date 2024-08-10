casa = float(input('Qual o valor da casa: '))
salario = float(input('Qual o salário do comprador: '))
tempo = int(input('Em quanto tempo a casa sera paga (anos): '))
meses = tempo * 12
prestação = casa / meses

print(f'Para pagar uma casa de R${casa:.2f} em {tempo} anos, o valor da prestação será de R${prestação:.2f}')

if (salario / 100 * 30) <= prestação:
    print('Empréstimo NEGADO! Você não atende os requisitos mínimos para comprar a casa.')
else:
    print('Empréstimo ACEITO! Aproveite sua casa nova.')
