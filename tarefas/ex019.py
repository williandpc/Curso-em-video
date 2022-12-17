###Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

a1 = input('insira o nome do primeiro aluno:')
a2 = input('insira o nome do segundo aluno:')
a3 = input('insira o nome do terceiro aluno:')
a4 = input('insira o nome do quarto aluno:')
lista = [a1,a2,a3,a4]
print(f' o aluno escolhido foi o(a) {random.choice(lista)}')

####para fazer listas colocar entre chaves as variaveis e o texto nao precisa de codigo
