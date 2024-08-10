tabela = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense', 'Athetico-PR',
          'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco da Gama', 'Bahia',
          'Santos', 'Goiás', 'Coritiba', 'América-MG')

print('-=-'*15)
print(f'Os times do Brasileirão são: {tabela}')

print('-=-'*15)
print('Os 5 primeiros são:')
for t in tabela[0:5]:
    print(t)

print('-=-'*15)
print('Os 4 últimos são:')
for t in tabela[-4:]:
    print(t)

print('-=-'*15)
print(f'Times em ordem alfabética: {sorted(tabela)}')

print('-=-'*15)
print(f'O São Paulo esta na {tabela.index("São Paulo") + 1}ª posição')
