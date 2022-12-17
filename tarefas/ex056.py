# Exercício Python 56:
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
it = 0
qm = 0
ih = 0
nameh = ''
lst = []
for c in range(1, 5):
   i = int(input(f'Digite a idade da {c}ª pessoa: '))
   name = input(f'Digite o nome da pessoa: ')
   sex = input(f'Digite o sexo da pessoa (homem/mulher): ')

   if sex.lower() == 'homem':
       if i > ih:
           ih = i
           nameh = name
   elif sex.lower() == 'mulher':
       qm += 1
       if i < 20:
           lst.append(name)
   else:
       print('Comece novamente, você não digitou corretamente')

   it += i
print(f"""A média de idades entre essas 4 pessoas é {it/4}
As mulheres com menos de 20 anos são {lst}     
E o homem mais velho é o {nameh}""")
