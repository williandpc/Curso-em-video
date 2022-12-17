# Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
print(f'Digite 3 números')
n1 = float(input('Nº 1: '))
n2 = float(input('Nº 2: '))
n3 = float(input('Nº 3: '))
if n1 == n2 == n3:
    print(f'Os números são iguais')
else:
    print(f""" O número menor é o {min(n1,n2,n3)}
    E o maior número é {max(n1,n2,n3)}""")
