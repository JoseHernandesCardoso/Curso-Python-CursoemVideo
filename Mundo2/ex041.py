from datetime import date

ano = date.today().year
ano_atleta = int(input('Ano de nascimento do atleta: '))
idade = ano - ano_atleta

if idade <= 9:
    categoria = 'MIRIM'
elif idade <= 14:
    categoria = 'INFANTIL'
elif idade <= 19:
    categoria = 'JUNIOR'
elif idade == 25:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'

print(f'O atleta tem {idade} anos de idade e se encaixa na categoria {categoria}.')