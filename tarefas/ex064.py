# Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
n = 0
soma = 0
count = 0
while n != 999:
    n = int(input('Digite um número inteiro // [para acabar o programa digite 999]: '))
    if n != 999:
        soma += n
        count += 1
print(f'Você digitou {count} números inteiros e a soma entre eles é {soma}')

