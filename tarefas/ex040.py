# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule a sua média,
# mostrando uma mensagem no final, conforme a média atingida:
#
# – Média abaixo de 5.0: REPROVADO
#
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
#
# – Média 7.0 ou superior: APROVADO

print('\033[36mOlá caro gafanhoto, qual foram as suas notas nesse periodo letivo?')
n1 = float(input('\033[34mDigite sua nota da A1: '))
n2 = float(input('Digite sua nota da A2: '))
media = (n1 + n2) / 2
if media < 5:
    print(f'\033[31:4mSua média final foi {media}, esta média está abaixo do necessario para aprovação ou contestação,'
          f' você esta reprovado ')
elif 5 <= media < 6.9:
    print(f'\033[33:1mSua média final foi {media},'
          f' você não atingiu o suficiente de aproveitamento para passar mas tem uma segunda chance,'
          f' você esta de recuperação ')
elif media > 7:
    print(f'\033[32:4mParabens gafanhoto!!! Você está aprovado com uma média de {media} ')