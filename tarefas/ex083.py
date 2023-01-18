# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

exp = input('Digite uma expressão qualquer: ')
abertos = 0
fechados = 0
for v in exp:
    if v in '()':
        


if exp.find('(') > exp.find(')') != -1 or exp.find('(') == -1:
    print('Os parênteses na expressão não foram abertos corretamente')
elif exp.find(')') == -1 or exp.find('(') < exp.find(')') != -1

