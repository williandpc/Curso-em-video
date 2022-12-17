# Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

# A) quantas pessoas tem mais de 18 anos.

# B) quantos homens foram cadastrados.

# C) quantas mulheres tem menos de 20 anos.
maiores = 0
homens = 0
mulheres = 0
c = 0
while True:
    print('_' * 20)
    print('CADASTRO PESSOAL')
    print('_' * 20)
    sexo = input('Digite o sexo[M/F]: ').strip().upper()[0]
    while sexo not in 'MF':
        sexo = input('Digite o sexo novamente[M/F]: ')
    idade = int(input('Digite sua idade: '))
    pro = input('Deseja continuar com o cadastro?[S/N]: ').strip().upper()[0]
    while pro not in 'SN':
        pro = input('Não entendi. Deseja continuar com o cadastro?[S/N]: ').strip().upper()[0]
    if idade > 18:
        maiores += 1
    if sexo.upper() == 'M':
        homens += 1
    if sexo.upper() == 'F':
        mulheres += 1
        if idade < 20:
            c += 1
    if pro.upper() == 'N':
        break
print('_' * 20)
print(f'CADASTRO FINALIZADO'.strip('==='))
print(f"""Temos {maiores} pessoa{'s'  if maiores != 1 else ''} maior{'es'  if maiores != 1 else ''} de 18 anos;
Das {homens + mulheres} pessoas cadastradas, temos {homens} home{'ns'  if homens != 1 else 'm'};
Das {homens + mulheres} pessoas cadastradas, temos {mulheres} mulher{'es'  if mulheres != 1 else 'm'},
das mulheres {c} delas tem menos de 20 anos""")
