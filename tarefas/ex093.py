# Exercício Python 093:
# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
jogador = {}
gols = []
jogador["nome"] = input('Nome do jogado: ')
jogos = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, jogos):
    gols.append(int(input(f'    Quantos gols na partida {c + 1}? ')))
jogador["gols"] = gols[:]
jogador["totals"] = sum(gols)
print('-=-'*30)
print(jogador)
print('-=-'*30)
for k,v in jogador.items():
    print(f'{k} = {v}')
print('-=-'*30)
print(f'O jogador {jogador["nome"]} jogou {jogos}.')
for j, g in enumerate(gols):
    print(f'    => Na partida {j + 1}, fez {g} gols.')
print(f'O total foi de {jogador["totals"]} gols')
