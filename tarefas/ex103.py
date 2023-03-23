def ficha(jogador, gols='0'):
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0

    print(f'O jogador {"<Desconhecido>" if not jogador.isalpha() else jogador} fez {gols} gol(s) no campeonato.')


ficha(jogador=str(input("Nome do jogador: ").strip()), gols=input("Número de gols: "))
