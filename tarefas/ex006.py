###Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n = int(input('insira um numero:'))
print(f'o dobro de {n} é {n*2}, o seu triplo recebe {n*3} e sua raiz quadrada recebe {(n**(1/2)):.0f}')
###":.0f" ajuda á retirar as casas decimais porem pode colocar a variavel em int tambem da no mesmo