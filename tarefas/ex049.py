#Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

"""###Exercício Python 9: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
num = int(input('digite um valor para a formação da tabuada:'))
print(f'a tabuada de {num} é \num'
      f'{num} x 1 = {num*1} \num'
      f'{num} x 2 = {num*2} \num'
      f'{num} x 3 = {num*3} \num'
      f'{num} x 4 = {num*4} \num'
      f'{num} x 5 = {num*5} \num'
      f'{num} x 6 = {num*6} \num'
      f'{num} x 7 = {num*7} \num'
      f'{num} x 8 = {num*8} \num'
      f'{num} x 9 = {num*9} \num'
      f'{num} x 10 = {num*10}')"""
n = int(input('Digite um valor: '))
print(f'A baixo você verá a tabuada do {n} :)')
for c in range(0, 11):
    print(f'{n} x {c} = {n*c}')
