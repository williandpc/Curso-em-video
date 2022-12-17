# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#
# [ 1 ] somar
#
# [ 2 ] multiplicar
#
# [ 3 ] maior
#
# [ 4 ] novos números
#
# [ 5 ] sair do programa
#
# Seu programa deverá realizar a operação solicitada em cada caso.

print('Para começarmos as opreções irei precisar que você digite 2 valores, entendido?')
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Agora, digite o segundo valor:'))
op = 0
while op != 5:
    op = int(input("""Qual operação você deseja fazer com os dois números?
[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa


Digite aqui sua escolha: """))
    if op == 1:
        print(f'Já que voce decidiu somar, o resultado da soma entre os dois números foi {n1 + n2}.', end=2*'\n')
    elif op == 2:
        print(f'Já que voce decidiu multiplicar, o produto entre os dois números é {n1 * n2}.', end=2*'\n')
    elif op == 3:
        print(f'Entre {n1} e {n2} o maior número é {max(n1,n2)}', end=2*'\n')
    elif op == 4:
        print('Okay vamos lá mudar os números')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Agora, digite o segundo valor:'))
    elif op == 5:
        print('Obrigado por usar nosso programa, ele será finalizado agora')
    if op != 5:
        print('Agora, deseja fazer outra operação?', end=2*'\n')
print('Ficou contente com as operações? Qualquer coisa é só rodar o programa novamente :)')
