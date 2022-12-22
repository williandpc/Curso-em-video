# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

"""Tuplas são imutavéis, não da para acrescentara nem tirar"""
from random import randint
num = ((randint(0, 100)), (randint(0, 100)), (randint(0, 100)), (randint(0, 100)), (randint(0, 100)))
print(f'Os números sorteados foram: ', end='')
for c in num:
    print(f'{c}', end=', ')
print(f"""\nO menor valor foi o {min(num)}
e o maior valor foi o {max(num)}""")

