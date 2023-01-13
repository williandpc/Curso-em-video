# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite o valor {c}: ')))
print(f'O maior valor foi {max(valores)} nas posições ', end='')
for i, v in enumerate(valores):
    if v == max(valores):
        print(f'{i}...', end='')
print(f'\nO menor valor foi {min(valores)} nas posições ', end='')
for i, v in enumerate(valores):
    if v == min(valores):
        print(f'{i}...', end='')