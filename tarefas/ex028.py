# Exercício Python 28: escreva um programa que faça o computador “pensar” num número inteiro entre 0 e 5
# e peça para o utilizador tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o utilizador venceu ou perdeu.

import random
import time
print('-=-' * 20)
print('Estou pensando em um numero de 0 a 5.')
n1 = int(input('Tente adivinhar qual número de 0 a 5 eu estou pensando: '))
print('Processando...')
time.sleep(3) ###biblioteca de tempo, codigo usado para pausar a execução da programação em num SEGUNDOS.
n2 = int(random.choice([0, 1, 2, 3, 4, 5]))
print('-=-' * 20)
if n1 == n2:
    print(f'DROGA >:( ! Você acertou parabéns! o número que eu escolhi também foi {n2}.')
else:
    print(f'GANHEI! Uma pena, você não lê mentes :(. eu escolhi {n2} e você escolheu {n1}')
