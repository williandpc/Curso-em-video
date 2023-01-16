# Exercício Python 082:
# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.
lista = []
pares = []
impares = []
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
    elif num % 2 != 0:
        impares.append(num)
    print('Números adicionados com sucesso! :)', end='')
    cont = input('Deseja continuar inserindo números [S/N]: ')
    while cont.lower()[0] != 's' and cont.lower()[0] != 'n':
        cont = input('Desculpe, não entend :(. Deseja continuar inserindo números [S/N]: ')
    if cont.lower()[0] == 'n':
        break
    elif cont.lower()[0] == 's':
        continue
print(f"""
Aqui está sua lista inteira: {lista}

Aqui está a lista contendo somente os números pares: {pares}

Aqui está a lista contendo somente os números impares: {impares}""")
