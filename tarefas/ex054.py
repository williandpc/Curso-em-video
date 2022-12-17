# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
import datetime

maiores = 0
menores = 0
for c in range(0, 7):
    s = int(input(f'Digite o ano de nascimento da {c+1}ª pessoa: '))
    idade = datetime.datetime.today().year - s
    print(f'Sua idade é de {idade} anos')
    if idade >= 18:
        maiores += 1
    else:
        menores += 1
print(f' Tem {maiores} pessoa(s) que é(são) maior(es) de idade.'
      f'Tem {menores} pessoa(s) que é(são) menor(es) de idade.')
