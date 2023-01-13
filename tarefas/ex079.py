# Exercício Python 079:
# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
lista = []
while True:
    new = (int(input('Digite um valor: ')))
    if new in lista:
        print(f'Valor duplicado! não irei adicionar...')
    else:
        lista.append(new)
        print(f'O valor {new} foi adicionado com sucesso!!!')
    keep = input('Deseja continuar? [S/N] ')
    while not keep[0].lower() in 'sn':
        keep = input('Desculpa, não entendi :( vamos tentar novamente. Deseja continuar? [S/N]  ')
    if keep[0].lower() == 'n':
        break
lista.sort()
print(f'Você digitou os valores {lista}')


