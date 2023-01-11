# Exercício Python 076:
# Crie um programa que tenha uma tupla única com nomes de produtos e os seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.
tupla = ('Arroz 1kg', 10.49,
         'Feijão 1kg', 5.55,
         'Sabonete Dove', 3.25,
         'Arroz integral 1kg', 5.50,
         'Salgadinho Doritoz 500g', 9.99,
         )
for n in range(0, len(tupla)):
    if n % 2 == 0:
        print(f'{tupla[n]:.<40}', end='')
    else:
        print(f'R${tupla[n]:>6.2f}')
