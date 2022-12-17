# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
#
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('='*20)
print('BANCO DPC')
print('='*20)
total = int(input("Qual valor você quer sacar? R$"))
valor = total
cedula = 50
t_cedula = 0
print(f"Voce irá receber:")
while True:
    if valor >= cedula:
        valor -= cedula
        t_cedula += 1
    else:
        if t_cedula != 0:
            print(f"{t_cedula} cédulas de R${cedula}")
        t_cedula = 0
        if valor == 0:
            break
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
print('Muito obrigado por escolher nosso banco!')
