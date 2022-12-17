# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
lista = []
for c in range(1, 6):
    p = float(input(f'Digite o peso da {c}º pessoa: '))

    lista.append(p)
maior = max(lista)
menor = min(lista)
print(f"""O maior peso lido foi de {maior}kg da {lista.index(max(lista)) + 1}ª pessoa.
E o maior peso lido foi de {menor}kg da {lista.index(min(lista)) + 1}ª pessoa.  """)
