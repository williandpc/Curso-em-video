# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
# primitivo e todas as informações possiveis sobre ele. (numerico, alfabetico, maiuscula etc...)
# aprendido pelo comando ".is..."
# PARA CAPITALIZAR = ".istitle"
x = input('digite algo:')
if x.isnumeric():
    x1 = int(x)
else:
    x1 = str(x)
print(f' O tipo primitivo dessa sentença é {type(x1)}')

###NOVO
print(f'{x} só contem espaços? {x.isspace()}')
print(f'{x} é somente numérico? {x.isnumeric()}')
print(f'{x} só contem algarismos? {x.isalpha()}')
print(f'{x} é alfanumérico? contém algarismos e letras? {x.isalnum()}')
print(f'{x} esta inteiramente em maiusculo? {x.isupper()}')
print(f'{x} esta inteiramente em minusculo? {x.islower()}')
print(f'{x} esta capitalizada? {x.istitle()}')