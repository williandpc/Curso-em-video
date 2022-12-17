# Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
#
# – à vista dinheiro/cheque: 10% de desconto
#
# – à vista no cartão: 5% de desconto
#
# – em até 2x no cartão: preço formal
#
# – 3x ou mais no cartão: 20% de juros

v = float(input('Qual foi o valor de sua compra? '))
choice = int(input("""Escolha uma opção de pagamento entre:
[1] À vista em dinheiro/cheque
[2] À vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão]
Sua escolha é? """))
if choice == 1:
    vt = v * 0.9  # desconto 10%
    print(f'Sua compra à vista no dinheiro/cheque recebe 10% de desconto,'
          f' dando um total de \033[32mR${v * 0.1} de desconto\033[m')
elif choice == 2:
    vt = v * 0.95  # desconto 5%
    print(f'Sua compra à vista no cartão recebe 5% de desconto,'
          f' dando um total de \033[32mR${v * 0.05} de desconto\033[m')
elif choice == 3:
    vt = v
    print(f'Parcelado em 2x no cartão o valor não altera ,'
          f' o valor de cada parcela será de \033[32mR${v/2}\033[m')
elif choice == 4:
    p = int(input('Digite a quantidade de parcelas desejadas: '))
    vt = v * 1.2 #20% juros
    print(f'Sua compra sera parcelada em {p}x, e terá 20% de juros.'
          f'Cada parcela tera um valor de \033[32mR${vt/p:.2f}\033[m')
else:
    print(f'\033[31;4mOpção inválida, selecione novamente!\033[m')
    vt = 'Nulo'
print(f'Sua compra de \033[32mR${v}\033[m vai sair no total de \033[32mR${vt}\033[m')
