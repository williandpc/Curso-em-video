# Exercício Python 087:
# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
matriz = [[], [], [], []]
for n in range(0, 3):
    for m in range(0, 3):
        numero = int(input(f'Digite um valor para [{n},{m}]: '))
        matriz[n].append(numero)
        if numero % 2 == 0:
            matriz[3].append(numero)
for n in range(0, 3):
    for m in range(0, 3):
        print(f'[{matriz[n][m]:^5}]', end=' ')
    print()
print(f"""Aqui etá a soma de todos os valores pares digitados: {sum(matriz[3])}.
Aqui está a soma dos valores da terceira coluna: {sum(matriz[c][2] for c in range(0, 3) )}.
Aqui está o maior valor da segunda coluna: {max(matriz[1][c] for c in range(0, 3) )}""")
