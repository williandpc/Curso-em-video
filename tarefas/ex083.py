# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

exp = str(input("Digite uma expressão qualquer: "))
pilha = []
for v in exp:
    if v == '(':
        pilha.append('(')
    elif v == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('parabens sua expressão esta corretamente indexada')
else:
    print('existem parentes não abertos/fechados corretamente')
