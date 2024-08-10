produto = float(input('Preço do produto: '))
print('-=-'*20)
print('''Formas de pagamento:
[ 1 ] À vista em dinheiro/cheque (10% de desconto)
[ 2 ] À vista no cartão (5% de desconto)
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão (20% de juros)
''')
pagamento = int(input('Forma de pagamento: '))
print('-=-'*20)

if pagamento == 1:
    preço = produto - (produto * 0.1 )
elif pagamento == 2:
    preço = produto - (produto * 0.05)
elif pagamento == 3:
    preço = produto
    print(f'O preço de cada parcela do produto, pago em 2x, será de R${preço/2:.2f}')
elif pagamento == 4:
    preço = produto + (produto * 0.2)
    parcela = int(input('Quantidade de parcelas: '))
    print(f'O preço de cada parcela do produto, pago em {parcela}x, será de R${preço/parcela:.2f}')
else:
    preço = produto
    print('OPÇÃO INVALIDA!')

print(f'O total a ser pago pelo produto sera de R${preço:.2f}')
