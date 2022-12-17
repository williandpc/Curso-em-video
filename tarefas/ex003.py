###Crie um programa que leia dois numeros e mostre a soma entre eles
x = int(input('digite um numero:'))
y = int(input('digite outro:'))
print(f'A soma entre {x} e {y} vale {x + y}')

#funciona com .format tambem

print('A soma entre {} e {} vale {}'.format(x, y, x+y))