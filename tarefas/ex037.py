#Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
n = int(input('Digite um numero inteiro qualquer: '))
bc = int(input("""Agora escolha qual base de conversão sera usada
         Binário [1]
         Octal [2]
         Hexadecimal [3]"""))
if bc == 1:
    tpcon ='Binário'
    nf = bin(n)
    print(f'O número digital ({n}), em conversão para {tpcon}  fica igual à {nf[2:]}')
elif bc == 2:
    tpcon = 'Octal'
    nf = oct(n)
    print(f'O número digital ({n}), em conversão para {tpcon}  fica igual à {nf[2:]}')
elif bc == 3:
    tpcon = 'Hexadecimal'
    nf = hex(n)
    print(f'O número digital ({n}), em conversão para {tpcon}  fica igual à {nf[2:]}')
else:
    print('\033[31:4mOpção invalida, tente novamente :(')
