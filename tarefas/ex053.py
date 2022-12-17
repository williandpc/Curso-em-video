# Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços. Exemplos de palíndromos:

# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
frase = input('Digite uma frase: ')
frase = frase.replace(' ', '')
print(frase)
print(frase[::-1])
if frase == frase[::-1]:
    print(f'A frase \033[35m{frase}\033[m é um palíndromo, pois seu contrario seria \033[35m{frase[::-1]}\033[m'
          f' E como o observado, a frase é a mesma.')
else:
    print(f'A frase \033[31m{frase}\033[m, não é um palíndromo, tendo como inverso a frase \033[31m{frase[::-1]}\033[m.'
          f' O inverso é uma frase totalmente diferente.')
