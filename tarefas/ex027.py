# Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

name = str(input("Digite um nome completo: ")).strip()
name1 = name.split()
print(f"Muito prazer em te conhecer {name}\n"
      f"Seu primeiro nome é {name1[0]} \n"
      f"O seu Segundo nome é {name1[len(name1) - 1]}")