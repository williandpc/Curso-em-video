# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

"""
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
"""

import random
import time
n1 = random.randint(0, 10)
n2 = int(input('Tente adivinhar qual é o número que eu estou pensando: '))
trys = 1
while n1 != n2:
    n2 = int(input(f'III ala ele, não acertou, o número {n2} não é a resposta. Tenta novamente: '))
    trys += 1
print(f"""Aeee você acertou, Parabéns!!! os números batem ambos escolhemos {n1 or n2}
Precisou tentar só {trys} vezes ein rsrsrs""")



