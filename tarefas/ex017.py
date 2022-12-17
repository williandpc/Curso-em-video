###Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto
# e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

##com import usando calculo para hipotenusa

'''import math
co = float(input('insira o comprimento do primeiro cateto: '))
ca = float(input('insira o comprimento do segundo cateto: '))
print(f'o valor do comprimento'
      f' hipotenusa de um triângulo retângulo de catetos com comprimentos equivalentes à {co} e {ca} '
      f'é igual à {math.hypot(ca,co)}')'''

###sem import usando calculo basico por extenso do proprio python

'''co = float(input('insira o comprimento do primeiro cateto: '))
ca = float(input('insira o comprimento do segundo cateto: '))
print(f'o valor do comprimento'
      f' hipotenusa de um triângulo retângulo de catetos com comprimentos equivalentes à {co} e {ca} '
      f'é igual à {(co**2 + ca**2)**(1/2)}')'''