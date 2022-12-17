#Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três
# e que se encontram no intervalo de 1 até 500.
s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        cont += 1
print(f'A contagem dos impares multiplos de 3 é igual à {cont}'
      f' a soma dos multiplos de 3 no intervalo de 1 a 500 é igual à {s}')