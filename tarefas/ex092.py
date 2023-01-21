# Exercício Python 092:
# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
import datetime
cadastro = {}
cadastro['nome'] = input('Nome: ')
cadastro['idade'] = datetime.date.today().year - int(input('Digite seu ano de nascimento: '))
cadastro['CTPS'] = int(input('Carteira de trabalho (0 caso não tenha): '))
if cadastro['CTPS'] != 0:
    cadastro['contratação'] = int(input('Ano de contratação: '))
    cadastro['salário'] = float(input('Sálario atual: R$'))
    cadastro['aposentadoria'] =(35 - (datetime.date.today().year - cadastro['contratação'])) + cadastro['idade']
print('--'*15)
for k, v in cadastro.items():
    print (f'-- {k}: {v}')