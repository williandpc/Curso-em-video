# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    print('Números adicionados com sucesso! :)', end='')
    cont = input('Deseja continuar inserindo números [S/N]: ')
    while cont.lower()[0] != 's' and cont.lower()[0] != 'n':
        cont = input('Desculpe, não entend :(. Deseja continuar inserindo números [S/N]: ')
    if cont.lower()[0] == 'n':
        break
    elif cont.lower()[0] == 's':
        continue
lista.sort(reverse=True)
print(f"""
Foram digitados {len(lista)} números.

Aqui está sua lista de forma decrescente {lista};

{"O valor 5 foi encontrado na lista." if lista.count(5) >= 1 else "O valor 5 não foi encontrado na lista"}
""")

    