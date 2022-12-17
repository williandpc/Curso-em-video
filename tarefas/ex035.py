# Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.
print('Digite o tamanho das retas separadamente')
print('-=-' * 20)
r = float(input('Digite o tamanho da reta 1: '))
print('-=-' * 20)
r2 = float(input('Digite o tamanho da reta 2: '))
print('-=-' * 20)
r3 = float(input('Digite o tamanho da reta 3: '))
print('-=-' * 20)
if r3 < (r + r2) and r2 < (r + r3) and r < (r2 + r3):
    print('As retas formam um triangulo')
else:
    print('As retas não formam um triangulo')