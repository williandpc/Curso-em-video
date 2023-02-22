from random import randint
from time import sleep
numeros = []


def sorteia():
    while len(numeros) != 5:
        numeros.append(randint(0, 10))
    print("Sorteando 5 valores da lista: ", end=' ')
    for num in numeros:
        print(num, end=' ')
        sleep(0.5)
    print("PRONTO!")


def somapar():
    s = 0
    for num in numeros:
        if num % 2 == 0:
            s += num
    print(f"Somando os valores pares de {numeros} temos {s}")


sorteia()
somapar()