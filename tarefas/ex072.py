
# -*- coding: iso-8859-15 -*-

tupla = (
    'zero', 'um', 'dois', 'tr�s', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
    'quartoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
)
while True:
    num = int(input("Para ver sua escrita em extenso, digite um n�mero de 0 a 20: "))
    while num not in range(0, 20):
        num = int(input("N�o entendi, vamos novamente\n"
                        "Para ver sua escrita em extenso, digite um n�mero de 0 a 20: "))
    print(f"Olha s�!! o n�mero que voc� digitou se escreve assim: {tupla[num]}")
    cont = input('Deseja Continuar[S/N]? ')
    while cont.upper()[0] != 'S' and cont.upper()[0] != 'N':
        cont = input('N�o entendi, voc� deseja Continuar?[S/N] ')
    if cont.upper()[0] == 'N':
        break
