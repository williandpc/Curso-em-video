# Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#
# – IMC abaixo de 18,5: Abaixo do Peso
#
# – Entre 18,5 e 25: Peso Ideal
#
# – 25 até 30: Sobrepeso
#
# – 30 até 40: Obesidade
#
# – Acima de 40: Obesidade Mórbida
p = float(input('Digite seu peso: '))
a = float(input('Digite sua altura: '))
imc = p / (a**2)
if imc > 18.5:
    s = 'Abaixo do peso'
elif 18.5 <= imc < 25:
    s = 'Peso ideal'
elif 25 <= imc < 30:
    s = 'Sobre peso'
elif 30 <= imc < 40:
    s = 'Obesidade'
elif imc > 40:
    s = 'Obesidade Mórbida'
print(f'Seu indice de massa corporal é de {imc:.2f} de acordo com a tabela, seu status se da como {s}')
