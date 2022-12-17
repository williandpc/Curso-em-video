# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia
# o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#
# – Até 9 anos: MIRIM
#
# – Até 14 anos: INFANTIL
#
# – Até 19 anos: JÚNIOR
#
# – Até 25 anos: SÊNIOR
#
# – Acima de 25 anos: MASTER

from datetime import date
y = int(input('\033[36mOlá atleta, insira seu ano de nascimento e colocaremos você em uma categoria: '))
age = date.today().year - y
if age <= 9:
    mod = 'Mirim'
elif 9 < age <= 14:
    mod = 'Infantil'
elif 14 < age <= 19:
    mod = 'Júnior'
elif 19 < age <= 25:
    mod = 'Sênior'
elif age > 25:
    mod = 'Master'
print(f'De acordo com sua idade de {age} anos, sua modalidade é: {mod}')


