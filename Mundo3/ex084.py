pessoas = list()
maior = menor = 0
while True:
    pessoa = list()
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    pessoas.append(pessoa[:])

    if pessoa[1] > maior:
        maior = pessoa[1]
    elif pessoa[1] < menor or menor == 0:
        menor = pessoa[1]

    c = str(input('Quer continuar? [S/N] ')).strip().upper()
    if c == 'N':
        break

pesado = list()
leve = list()
for p in pessoas:
    if p[1] == maior:
        pesado.append(p[0])
    elif p[1] == menor:
        leve.append(p[0])

print('-=-'*15)
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'O maior peso registrado foi de {maior:.1f}Kg. Que é o peso de {pesado}')
print(f'O menor peso registrado foi de {menor:.1f}Kg. Que é o peso de {leve}')
