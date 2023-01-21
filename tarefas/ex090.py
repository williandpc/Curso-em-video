# Exercício Python 090:
# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.
cadastro = {}
cadastro['Nome'] = input('Digite o nome do aluno: ')
cadastro['Nota'] = float(input(f'Digite qual foi a media de {cadastro["Nome"]}: '))
cadastro['Situação'] = 'Reprovado' if (cadastro['Nota'] < 7) else 'Aprovado'
for k, v in cadastro.items():
    print(f'{k} = {v}')