# Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
n = ''
while n.upper() != 'M' and n.upper() != 'F':
    n = input('Digite seu sexo [M/F]: ')
    if n.upper() != 'M' and n.upper() != 'F':
        print('Não consegui compreender, tente novamente :)')
print(f'Sexo {n.upper()} registrado com sucesso')
