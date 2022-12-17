# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

import random

print("""Escolha dentre as opções:
 [1] PEDRA
 [2] PAPEL
 [3] TESOURA""")
itens = ('Pedra', 'Papel', 'Tesoura')
play = int(input('Escolha sua jogada: ')) - 1
pc = random.randint(0, 2)
if 0 == play and pc == 2 or play == 1 and pc == 0 or play == 2 and pc == 1:
    print(f'\033[4;32mParabéns!!! você me venceu!!'
          f' eu escolhi {itens[pc]} que foi derrotado pelo(a) seu(a) {itens[play]}\033[m')
elif play == pc:
    print(f'\033[36;4mParece que chegamos a um impasse cowboy.... ambos escolhemos {itens[play or pc]}\033[m')
elif play == 0 and pc == 1 or play == 1 and pc == 2 or play == 2 and pc == 0:
    print(f'\033[31:1mQue peninha,'
          f' parece que eu previ seus movimentos e venci seu(a) {itens[play]} com {itens[pc]} \033[m')
else:
    print('Desculpa essa não é uma opção :( tente novamente')
