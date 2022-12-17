# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random
qnt = 0
wins = 0
while True:
    print('-='*20)
    print('PAR OU IMPAR?')
    print('-='*20)
    player = int(input('Digite um valor [0 a 10]: '))
    computer = random.randint(0, 10)
    pi = input('Voce quer ser par ou impar? [P/I]: ')
    while pi.upper() not in 'PI':
        pi = input('Desculpa, nao entendi. Voce quer ser par ou impar? [P/I]: ')
    if (player + computer) % 2 == 0 and pi.upper() == 'I' or (player + computer) % 2 != 0 and pi.upper() == 'P':
        break
    print('_' * 20)
    print(f"Parabens mulecote!!! voce venceu com {'par'  if pi.upper() == 'P' else 'impar'}."
          f" eu tirei {computer} e você {player} somando em {player + computer}")
    print('_' * 20)
    wins += 1
print('_' * 20)
print(f"HA! Você perdeu!! voce perdeu por escolher {'par'  if pi.upper() == 'P' else 'impar'},"
      f" eu tirei {computer} e você {player} totalizando em {player + computer}."
      f" Mas olha, você conseguiu ganhar {wins} rodada{'s'  if wins != 1 else ''} seguida{'s'  if wins != 1 else ''}! ")
