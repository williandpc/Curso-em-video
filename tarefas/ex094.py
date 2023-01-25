# Exercício Python 094:
# Crie um programa que leia nome,
# sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
cadastro = []
pessoa = {}
while True:
    pessoa["nome"] = input('Nome: ')
    pessoa["sexo"] = input('Sexo[M/F]: ')[0].upper()
    while pessoa["sexo"][0].upper() not in 'MF':
        pessoa["sexo"] = input('Desculpa não entendi, vamos tentar novamente. \nDigite o seu sexo(somente M ou F): ')
    pessoa["idade"] = float(input('Idade: '))
    cadastro.append(pessoa.copy())
    replay = input("Quer continuar o cadastro? [S/N]")
    while replay[0].upper() not in 'NS':
        replay = input('Desculpa não entendi, vamos tentar novamente. \nDeseja continuar o cadastro?(somente S ou N): ')
    if replay[0].upper() == 'N':
        break
media = (sum(cadastro[c]["idade"] for c in range(0, len(cadastro)))) / len(cadastro)
print(f'A) Foram cadastradas {len(cadastro)} pessoas')
print(f'B) A média da faixa etária é de:'
      f' {media}')
print(f'C) As mulheres são: ', end='')
for v in cadastro:
    if v["sexo"][0].upper() == 'F':
        print(v["nome"], end=' ')
print()
print(f'D) As pessoas com idade acima da média são: ', end='')
for v in cadastro:
    if v["idade"] > media:
        print(f'    =>nome:{v["nome"]} =>Idade: {v["idade"]}', end='')
