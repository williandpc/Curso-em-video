#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print('\033[36mAntes de finalizar o orçamento irei precisar de algumas informações, tudo bem?')
c = float(input('primeiro, o valor da casa é de? R$'))
s = float(input('segundo, o seu salario é de? R$'))
a = float(input('terceiro, em quantos anos pretende pagar?'))
p = c/(a*12)
if  p/s > 30/100:
    print(f'seu pedido de empréstimo foi negado')
else:
    print(f'\033[31;4mParabéns!!!\033[m, seu empréstimo foi aprovado com {a*12} parcelas de R${p} cada.')
