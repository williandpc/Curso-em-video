# ##Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e em que posição aparece a última vez

frase = input("Digite uma frase:")
print(f"A letra 'A' aparece {frase.upper().count('A')} vez(es)")
print(f"A letra 'A' aparece inicialmente na posição  {frase.upper().find('A') + 1}")
print(f"A letra 'A' aparece ultimamente na posição  {frase.upper().rfind('A') + 1}") ###começando a buscar a partir do lado direito
