# Exercício Python 66: Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

soma = 0
cont = 0
while True:
    n = int(input('Digite a quantidade de valores que você desejar[999 para parar.]: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'a soma dos {cont} números digitados deu {soma}')
