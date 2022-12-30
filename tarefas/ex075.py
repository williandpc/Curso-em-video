# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre:
#
# A) Quantas vezes apareceu o valor 9.
#
# B) Em que posição foi digitado o primeiro valor 3.
#
# C) Quais foram os números pares.

tupla = (int(input('Digite o 1º valor: ')),
int(input('Digite o 2º valor: ')),
int(input('Digite o 3º valor: ')),
int(input('Digite o 4º valor: ')))
if tupla.count(9):
    print(f'O valor 9 apareceu {tupla.count(9)} vez(es).')
else:
    print('Não existe o valor 9 na tupla.')
if tupla.count(3):
    print(f'O primeiro valor 3 foi digitado no {tupla.index(3) + 1}º valor')
else:
    print(f'Não existe valor 3 na tupla.')
print(f'Os números pares da tupla são:', end=' ')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')
