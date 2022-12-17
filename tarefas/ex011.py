# ##Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e
# a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
l = int(input('Digite a largura da parede em metros:'))
a = int(input('Digite a altura da parede em metros:'))
A = a * l
print(f' a area da parede é de {A}m² e será necessario {float(A / 2)} litros de tinta')
