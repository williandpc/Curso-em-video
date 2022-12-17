# ##Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
# (1)O nome com todas as letras maiúsculas
# (2)O nome com todas as letras minúsculas
# (3)Quantas letras ao todo (sem considerar espaços)
# (4)Quantas letras tem o primeiro nome
frase = input('Digite seu nome completo:')
# (1):
print(f'Seu nome todo em maiúsculo fica:{frase.upper().strip()} ')
# (2):
print(f'Seu nome todo em minúsculo fica:{frase.lower().strip()} ')
# (3):
frase2 = frase.replace(' ', '')
print(f'O seu nome completo tem {len(frase2)} letras desconsiderando os espaços')
# (4):
frase3 = frase.split()
print(f'seu primeiro nome é {frase3[0]} e tem {len(frase3[0])} letras')

