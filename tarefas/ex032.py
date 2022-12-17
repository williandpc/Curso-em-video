# Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
y = int(input('Digite um ano: '))
if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
    print(f'O ano {y} é bissexto.')
else:
    print(f'O ano {y} não é bissexto')









