# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos,
# acrescentando o recurso de mostrar que tipo de triângulo será formado:
#
# – EQUILÁTERO: todos os lados iguais
#
# – ISÓSCELES: dois lados iguais, um diferente
#
# – ESCALENO: todos os lados diferentes

print('Digite o tamanho das retas separadamente')
print('-=-' * 20)
r = float(input('Digite o tamanho da reta 1: '))
print('-=-' * 20)
r2 = float(input('Digite o tamanho da reta 2: '))
print('-=-' * 20)
r3 = float(input('Digite o tamanho da reta 3: '))
print('-=-' * 20)
if r3 < (r + r2) and r2 < (r + r3) and r < (r2 + r3):
    print('As retas formam um triangulo')
    if r3 == r2 != r or r3 == r2 != r or r2 == r != r3:
        tipo = 'Equilátero'
    elif r3 == r2 == r3:
        tipo = 'isósceles'
    elif r3 != r2 != r3:
        tipo = 'escaleno'
    print(f'O trangulo formado será um triângulo {tipo}')
else:
    print('As retas não formam um triangulo')