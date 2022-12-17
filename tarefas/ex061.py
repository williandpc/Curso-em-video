# Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

"""#Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
print('='*20)
print('10 TERMOS DE UMA PA.')
print('='*20)
s = int(input('Primeiro Termo:'))
cont = s
razao = int(input('Razão: '))
for c in range(s, s+10):

    print(f'{cont}', end='→ ')
    cont += razao
"""

count = 0
n = int(input('Digite o primeiro termo da Progressão: '))
r = int(input('Agora a razão: '))
while count <= 10:
    count += 1
    if count < 10:
        print(f'{n}', end='→ ')
    elif count == 10:
        print(f'{n}')
    n += r

