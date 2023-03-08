def ficha(jogador='<Desconhecido>', gols='0'):
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato.')


ficha(jogador=str(input("Nome do jogador: ").lstrip()), gols=input("Número de gols: "))
