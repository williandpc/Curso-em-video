# Exercício Python 34:Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
rs = float(input('Digite o seu salário: R$'))
if rs > 1250:
    print(f'Seu aumento será de R${rs * 0.1} totalizando um salário de R${rs * 1.1:.2f}')
if rs <= 1250:
    print(f'Seu aumento será de R${rs * 0.15} totalizando um salário de R${rs * 1.15:.2f}')