def ficha(jogador='<Desconhecido>', gols=0):
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato.')


ficha(input("Nome do jogador: "), int(input("Número de gols: ")))
