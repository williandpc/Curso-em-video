# Exercício Python 088:
# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.
import random
import time
lista = []
print('='*30)
print('LOTERICAS WILLIAN & NAGAMINE'.center(30))
print('jogos da mega cena'.center(30, '.'))
print('='*30)
qntd = int(input('Quantos jogos você ira sortear? '))
print('='*30)
print(f'SORTEANDO {qntd} JOGOS'.center(30, '¨'))
for jogos in range(0, qntd):
    while len(lista) != 6:
        num = random.randint(1, 60)
        lista.append(num) if num not in lista else ''
    lista.sort()
    print(f'Jogo {jogos + 1}: {lista}')
    time.sleep(2)
    lista.clear()
print(f'BOA SORTE'.center(30, '¨'))
