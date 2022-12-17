# Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

km = float(input("digite a distância em km da sua viagem: "))
if km <= 200:
    print(f'Como a viagem menor de 200km é consderada curta, '
          f'o valor da sua passagem será de R${km*0.5}.')
else:
    print(f'Como sua viagem é considerada longa,'
          f'o valor da sua passagem será de R${km*0.45}')
print('Viaje conosco e se divirta!')