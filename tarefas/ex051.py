#Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
print('='*20)
print('10 TERMOS DE UMA PA.')
print('='*20)
s = int(input('Primeiro Termo:'))
cont = s
r = int(input('Razão: '))
for c in range(s, s+10):

    print(f'{cont}', end='→ ')
    cont += r
