# Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

v = int(input('Digite um numero inteiro: '))
v1 = v % 2
if v1 == 1:
    print(f'O número {v} é ÍMPAR!')
else:
    print(f'O número {v} é PAR!')