# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
valor = []
w = ''
soma = 0
while w.upper() != 'N':
    n = int(input('Digite um valor inteiro: '))
    valor.append(n)
    soma += n
    w = input('Deseja digitar um novo valor? [S/N]:')
    while w.upper() != 'S' and w.upper() != 'N':
        w = input('Desculpe, não entendi. Deseja continuar? [S/N]:')
print(f"""A média entre os {len(valor)} valores foi de {int(soma / len(valor))}.
O maior valor foi {max(valor)}.
O menor valor foi {min(valor)}.""")

