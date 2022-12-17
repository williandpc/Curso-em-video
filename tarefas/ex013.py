# ##Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário,
# com 15% de aumento.
s = float(input('digite seu salario:'))
a = s*0.15
##a == acrescimo
print(f'seu novo salario sera de R${s+a:.2f}')