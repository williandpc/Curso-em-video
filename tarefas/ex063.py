# Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer
# e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8
print('='*30)
print('Sequencia de Fibonacci')
print('='*30)
lim = int(input('Digite quantos elementos você deseja ver da Sequência de Fibonacci: '))
count = 3
n1 = 0
n2 = 1
print('='*30)
print(f'{n1} → {n2}', end='')
while count <= lim:
    n3 = n1 + n2
    print(f' → {n3}', end='')
    count += 1
    n1 = n2
    n2 = n3
print('\nFIM')



