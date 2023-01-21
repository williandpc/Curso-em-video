# Exercício Python 089:
# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um
# e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""COM A LISTA GUARDANDO O BOLETIM DOS ALUNOS"""

boletim = [[], [], []]
while True:
    boletim[0].append(input('Nome: '))
    boletim[1].append(float(input('Nota P1: ')))
    boletim[2].append(float(input('Nota P2: ')))
    cc = (input('Deseja continuar cadastrando alunos[S/N]? '))
    while cc[0].lower() not in 'sn':
        cc = input('Desculpa não entendi, vamos tentar novamente? Deseja continuar cadastrando alunos[S/N]? ')
    if cc[0].lower() == 'n':
        break
print('='*19)
print(f'No.'.ljust(4), end='')
print(f'NOME'.ljust(10), end='')
print(f'MÉDIA'.ljust(4))
print('-'*19)
for i in range(0, len(boletim[0])):
    print(f'{i:<4}{boletim[0][i]:<20}{((boletim[1][i] + boletim[2][i]) / 2).__round__(1) :>4}')
print('='*19)
while True:
    n = input("""De quem você gostaria de ver as notas brutas? 
Digite o seu numero da lista ou o seu nome. [9999 interrompe]. """).lower()
    if int(n) == 9999:
        break
    else:
        if n.isnumeric():
            print(f'As notas de {boletim[0][n]} separadamente são: '
                  f'{boletim[1][n]} e {boletim[2][n]}.')
        else:
            ia = boletim[0].index(n)
            print(f'As notas de {(boletim[0][ia])}'
                  f'separadamente são: {boletim[1][ia]} e {boletim[2][ia]}.')
    print('=' * 19)
print(f'FINALIZANDO.....')
print(f'Muito obrigado!! Estou disponivel para mais consulta!!!')
