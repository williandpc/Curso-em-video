#Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
n = int(input('Digite um numero:'))
cont = 0
for c in range(1, n+1):
    if  n % c == 0:
        print('\033[32m', end=' ')
        cont += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}\033[m', end=' ')
if cont == 2:
    print(f'\n O número {n} número é um numero primo!')
else:
    print(f'\n O número {n} não é um número primo!')
