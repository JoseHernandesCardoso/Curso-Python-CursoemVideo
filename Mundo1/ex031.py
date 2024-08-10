dis = float(input('Qual a distancia da viajem (Km): '))
if dis <= 200:
    preço = dis * 0.5
else:
    preço = dis * 0.45

print(f'O custo da viajem é de R${preço:.2f}')
