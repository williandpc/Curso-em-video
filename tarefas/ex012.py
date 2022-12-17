###Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
p = float(input('qual o valor do produto?'))
print(f'o valor novo do produto com 5% de desconto sera de {p * (1 - 5 / 100)}')
## OU
print(f'o valor novo do produto com 5% de desconto sera de {p * (95 / 100)}')
## OU
print(f'o valor novo do produto com 5% de desconto sera de {p - p * 0.05}')
## OU
d = p * 0.05
print(f'o valor novo do produto com 5% de desconto sera de {p - d}')
