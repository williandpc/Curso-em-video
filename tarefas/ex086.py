# Exercício Python 086:
# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
matriz = [[], [], []]
for n in range(0, 3):
    for m in range(0, 3):
        matriz[n].append(int(input(f'Digite um valor para [{n},{m}]: ')))
for n in range(0, 3):
    for m in range(0, 3):
        print(f'[{(matriz[n][m]):^5}]', end=' ')
    print()