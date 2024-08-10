def ficha(jogador='<desconhecido>', gols=0):
    if jogador == '':
        jogador = '<desconhecido>'
    if gols == '':
        gols = 0
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato')


ficha(str(input('Nome do jogador: ')),
      str(input('Número de gols: ')))
