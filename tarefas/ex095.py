# Exercício Python 095:
# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
time = []
jogador = {}
gols = []
while True:
    jogador["nome"] = input('Nome do jogado: ')
    jogos = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, jogos):
        gols.append(int(input(f'    Quantos gols na partida {c + 1}? ')))
    jogador["gols"] = gols[:]
    jogador["totals"] = sum(jogador["gols"])
    time.append(jogador.copy())
    gols.clear()
    replay = input("Quer continuar o cadastro? [S/N]")
    while replay[0].upper() not in 'NS':
        replay = input('Desculpa não entendi, vamos tentar novamente. \nDeseja continuar o cadastro?(somente S ou N): ')
    if replay[0].upper() == 'N':
        break
print('-=-'*30)
print(f"{'cod':>5}", end='')
for key, value in jogador.items():
    print(f"{key:>10}", end='')
print()
print('-=-'*30)
for i, player in enumerate(time):
    print(f'{i:>5}', end='')
    for k, v in player.items():
        print(f'{str(v):>10}', end='')
    print()
print('-=-'*30)
while True:
    status = int(input("Mostrar dados de qual jogador? [999 para cancelar] "))
    if status == 999:
        break
    print(f'Levantamento do jogador {time[status]["nome"].upper()}:')
    for i, v in enumerate(time[status]["gols"]):
        print(f"    => No jogo {i + 1} fez {v} gol(s)")
