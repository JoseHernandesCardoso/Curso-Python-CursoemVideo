from datetime import date

idade = int(input('Digite a sua idade: '))
ano = date.today().year
if idade < 18:
    alistamento = (18 - idade) + ano
    print(f'Você não tem idade para fazer o alistamento militar.\nO seu alistamento será no ano de {alistamento}.')
elif idade == 18:
    print('Está na hora de fazer o seu alistamento militar.')
else:
    alistamento = ano - (idade - 18)
    print(f'Você já realizou seu alistamento militar.\nO seu alistamento ocorreu em {alistamento}.')