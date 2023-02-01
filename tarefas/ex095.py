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
    print(f'{i:>5}', end='  ')
    for v in player:
        print(f'{v:>10}', end='')
    print()
print('-=-'*30)
#    print(f'O jogador {jogador["nome"]} jogou {jogos}.')
#for j, g in enumerate(jogador["gols"]):
#    print(f'    => Na partida {j + 1}, fez {g} gols.')
#print(f'O total foi de {jogador["totals"]} gols')
