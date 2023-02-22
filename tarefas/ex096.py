# Exercício Python 096: Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(l, h):
    a = l * h
    print(f'A área de um terreno de {h} x {l} é de {a}m²')


area(float(input('LARGURA (m): ')), float(input('COMPRIMENTO (M):')))
