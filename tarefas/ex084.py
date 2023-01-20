# Exercício Python 084:
# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

galera = []
pepe = []
print('CADASTRO PESSOAL'.center(30, '='))
while True:
    print('Nova Pessoa'.center(30, '='))
    pepe.append(input('Nome: '))
    pepe.append(float(input('Peso: ')))
    galera.append(pepe[:])
    pepe.clear()
    again = input('Deseja continuar o cadastro[S/N]? ')
    while 'N' != again.lstrip().upper()[0] != 'S':
        again = input('Desculpa não entendi, vamos tentar novamente? Deseja continuar o cadastro[S/N]? ')
    if again.rstrip().upper()[0] == 'N':
        break
    elif again.rstrip().upper()[0] == 'S':
        continue
print(f'Foram cadastradas {len(galera)} pessoas.')
menor = min(m[1] for m in galera)
print(f'Dentre essas pessoas, o menor peso cadastrado foi {menor}kg dessas pessoas: ', end='')
for pessoa in galera:
    if pessoa[1] == menor:
        print(pessoa[0], end=' ')
print()
maior = max(mai[1] for mai in galera)
print(f'Dentre essas pessoas, o maior peso cadastrado foi {maior}kg dessas pessoas: ', end='')
for pessoa in galera:
    if pessoa[1] == maior:
        print(pessoa[0], end=' ')
