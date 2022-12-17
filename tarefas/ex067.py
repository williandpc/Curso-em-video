# Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
while True:
    t = int(input('Quer ver a tabuada de qual valor? '))
    print('_'*20)
    if t < 0:
        break
    print(f"""{t} x 1 = {t*1}
{t} x 2 = {t*2}
{t} x 3 = {t*3}
{t} x 4 = {t*4}
{t} x 5 = {t*5}
{t} x 6 = {t*6}
{t} x 7 = {t*7}
{t} x 8 = {t*8}
{t} x 9 = {t*9}
{t} x 10 = {t*10}""")
    print('_'*20)
print('Prontinho, terminamos :)')

# forma feita na resolução contendo o for dentro do while eterno
while True:
    t = int(input('Quer ver a tabuada de qual valor? '))
    if t < 0:
        break
    print('_'*20)
    for c in range(1, 11):
        print(f'{t} x {c} = {c * t}')
    print('_'*20)
print('Prontinho, terminamos :)')
# Jeito mais simples para reproduzir o exercicio
