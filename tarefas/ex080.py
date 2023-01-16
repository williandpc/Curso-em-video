# Exercício Python 080:
# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
tipo = input('Digite qual solução voce vai querer acessar [1/2]: ')
if tipo == '1':
    lista = []
    listaf = []
    for c in range(0, 5):
        num = int(input('Digite um valor: '))
        lista.append(num)
    for c in range(0, 5):
        listaf.append(min(lista))
        lista.remove(min(lista))
    print(f'sua lista ordenada fica {listaf}')
elif tipo == '2':
    lista = []
    for c in range(0, 5):
        num = int(input('Digite um valor: '))
        if len(lista) == 0 or num > lista[-1]:
            lista.append(num)
        else:
            i = 0
            while i < len(lista):
                if num < lista[i]:
                    lista.insert(i, num)
                    break
                i += 1
    print(f'sua lista ordenada fica {lista}')
    