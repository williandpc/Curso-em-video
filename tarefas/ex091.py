# Exercício Python 091:
# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from time import sleep
from random import randint
from operator import itemgetter
dicionario = {}
print('Valores sorteados: ')
for qntd in range(0, 4):
    dicionario[f'Jogador{qntd + 1}'] = randint(1, 6)
for jogador, vdado in dicionario.items():
    print(f'    O {jogador} tirou {vdado}')
    sleep(1)
print('Ranking dos jogadores: ')
"""MEU METODO ABAIXO"""
#for c in range(0, 4):
#    for j, v in dicionario.items():
#        if v == max(dicionario.values()):
#            print(f"    {c + 1}º lugar: {j} com o valor {v} ")
#            del dicionario[j]
#            break
#    sleep(1)
"""METODO GUANABARA ABAIXO"""
dicionario = sorted(dicionario.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(dicionario):
    print(f"    O {i + 1}º lugar: {v[0]} com {v[1]}.")
    sleep(1)
