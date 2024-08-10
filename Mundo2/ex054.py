from datetime import date

maior = 0
menor = 0
for c in range(1, 8):
    ano = date.today().year
    pessoa = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    if ano - pessoa >= 21:
        maior += 1
    else:
        menor += 1
print(f'No total das 7 pessoas, {maior} são maiores de idade (maior de 21 anos) e {menor} são menores de idade (menores de 21 anos)')
