# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
#
# 5! = 5 x 4 x 3 x 2 x 1 = 120
import math

count = int(input('Calculo da fatorial: '))

n = count

print(f'{count}! =', end=' ')
while n != 1:
    if n != 1:
        print(f' {n} x', end=' ')
    elif n == 1:
        print(f' {n}', end=' ')
    n -= 1
print(f' = {math.factorial(count)}')
