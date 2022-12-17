
# -*- coding: iso-8859-15 -*-

tupla = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
    'quartoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
)
while True:
    num = int(input("Para ver sua escrita em extenso, digite um número de 0 a 20: "))
    while num not in range(0, 20):
        num = int(input("Não entendi, vamos novamente\n"
                        "Para ver sua escrita em extenso, digite um número de 0 a 20: "))
    print(f"Olha só!! o número que você digitou se escreve assim: {tupla[num]}")
    cont = input('Deseja Continuar[S/N]? ')
    while cont.upper()[0] != 'S' and cont.upper()[0] != 'N':
        cont = input('Não entendi, você deseja Continuar?[S/N] ')
    if cont.upper()[0] == 'N':
        break
