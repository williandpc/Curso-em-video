#Exercício Python 50:
# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

soma = 0
cont = 0
for c in range(0, 6):
    n = int(input(f'Digite o {c + 1}º valor:'))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f' Você digitou {cont} numeros pares.'
      f' A soma total dos números pares que foram digitados é igual à {soma}')