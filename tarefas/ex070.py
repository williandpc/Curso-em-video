# Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#
# A) qual é o total gasto na compra.
#
# B) quantos produtos custam mais de R$1000.
#
# C) qual é o nome do produto mais barato.

total = 0
maoires = 0
c = ''
cheap = 0
valores = []
while True:
    print('=' * 20)
    print('Mercados DPC')
    print('=' * 20)
    nome = input('Digite o nome do produto: ')
    valor = float(input('Digite o valor do produto[R$]: '))
    total += valor
    if valor > 1000:
        maoires += 1
    valores.append(valor)
    if min(valores) == valor:
        c = nome
        cheap = valor
    final = input('Deseja continuar com as compras?[S/N]: ').strip().upper()[0]
    while final not in 'SN':
        final = input('Não entendi. Deseja continuar com as compras?[S/N]: ').strip().upper()[0]
    if  final.upper() == 'N':
        break
print('=' * 20)
print(f""" Obrigado por comprar conosco, Volte sempre!!!
O total de suas compras deu R${total}.
Existem {maoires} itens que custam mais de R$1000,00.
Mas olha só, você tem um produto baratissimo aqui, sua compra mais barata, a(o) {c} custando apenas R${cheap}.""")




