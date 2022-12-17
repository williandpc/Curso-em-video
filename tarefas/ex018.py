###Exercício Python 18: Faça um programa que leia um ângulo qualquer
# e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
a = math.radians(float(input('Digite o ângulo que você deseja: ')))
print(f'o seno desse angulo é {math.sin(a):.2f} \n'
      f'o cosceno desse angulo é {math.cos(a):.2f} \n'
      f'e a tangente desse angulo é {math.tan(a):.2f}')