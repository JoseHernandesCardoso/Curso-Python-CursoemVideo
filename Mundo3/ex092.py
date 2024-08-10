from datetime import date

ano = date.today().year

pessoa = dict()
pessoa['Nome'] = str(input('Nome: '))
pessoa['Idade'] = ano - int(input('Ano de nascimento: '))
pessoa['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['CTPS'] != 0:
    pessoa['Contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salário: '))
    pessoa['Aposentadoria'] = pessoa['Idade'] + (35 - (ano - pessoa['Contratação']))

print('-=-'*15)
for k, v in pessoa.items():
    print(f'{k} tem valor {v}')
