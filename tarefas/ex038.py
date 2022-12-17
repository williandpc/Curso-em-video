# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#
# – O primeiro valor é maior
#
# – O segundo valor é maior
#
# – Não existe valor maior, os dois são iguais

print('\033[33mOlá, para o exercicio continuar irei precisar de dois numeros inteiros')
print('-=-'*30)
n1 = int(input('\033[36mDigite o primeiro valor: '))
print('-=-'*30)
n2 = int(input('\033[36mDigite o segundo valor: '))
print('-=-'*30)

if n1>n2:
    print(f'\033[36mO número {n1} é maior que o numero {n2}')
elif n2 > n1:
    print(f'\033[36mO número {n2} é maior que o numero {n1}')
elif n1 == n2:
    print(f'\033[31;4mNão existe maior entre {n1} e {n2}, os dois valores são iguais.')