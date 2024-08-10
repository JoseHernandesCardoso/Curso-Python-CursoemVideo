def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
         votar = 'VOTO NEGADO'
    elif 16 <= idade < 18 or idade >= 65:
        votar = 'VOTO OPCIONAL'
    elif 18 <= idade < 65:
        votar = 'VOTO OBRIGATÓRIO'

    return f'Com {idade} anos: {votar}'


anonasc = int(input('Em que ano você nasceu? '))
print(voto(anonasc))