produtos = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20,
            'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-'*39)
print(f'{"LISTAGEM DE PREÇOS":^39}')
print('-'*39)

for item in range(0, len(produtos), 2):
    print(f'{produtos[item]:.<30}R${produtos[item+1]:>7.2f}')

print('-'*39)
