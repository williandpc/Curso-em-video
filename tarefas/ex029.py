# Exercício Python 29: escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.
v = float(input('Digite a velocidade do carro: '))
if v <= 80:
    print(f"Parabéns, você está dentro do limite de velocidade!. Continue sendo um bom condutor :)")
else:
    multa = (v - 80) * 7
    print(f"""Tãoooooo triste, você estava acima do limite de velocidade e recebera uma multa :(.
sua multa sera de R${multa:.2f}""")
