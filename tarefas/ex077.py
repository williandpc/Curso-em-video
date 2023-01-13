# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

tupla = (
    'Amor',
    'Paralelepipedo',
    'Cama',
    'Cebola',
    'Colher',
    'Cadeira',
    'Luz'
    )

for palavras in tupla:
    print(f'Na palavra "{palavras}" tem as vogais: ', end='')
    for letra in palavras:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end='')
    print(end='\n')

