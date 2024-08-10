print('='*30)
print(f'{"LOJA SUPER BARATÃO":^30}')
print('='*30)

total = n_muito_caro = barato_preco = 0
barato_nome = ''
while True:
    continua = ''

    nome = input('Nome do produto: ')
    preco = int(input('Preço: R$'))
    while continua not in ['S', 'N']:
        continua = input('Quer continuar? [S/N] ').strip().upper()[0]

    total += preco
    if preco > 1000:
        n_muito_caro += 1

    if barato_nome == '' or preco < barato_preco:
        barato_preco = preco
        barato_nome = nome

    if continua == 'N':
        break
    print('='*30)

print(f'{"FIM DO PROGRAMA":-^30}')
print(f'O total da compra foi de R${total:.2f}')
print(f'Temos {n_muito_caro} produtos que custam mais de R$1000.00')
print(f'O produto mais barato foi {barato_nome} que custa R${barato_preco:.2f}')
