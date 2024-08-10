from math import hypot

opos = float(input('tamanho do cateto oposto: '))
adj = float(input('tamanho do cateto adjacente: '))
hip = hypot(opos, adj)

print(f'A hipotenusa do triangulo mede {hip:.2f}')
