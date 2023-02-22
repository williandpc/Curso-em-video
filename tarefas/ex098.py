# Exercício Python 098:
# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada


from time import sleep

def contador(inicio, fim, passo):
        print('-='*16)
        if passo < 0:
            passo *= -1
        elif passo == 0:
            passo = 1
        print(F"CONTAGEM de {inicio} até {fim} de {passo} em {passo}")
        num = inicio
        sleep(0.5)
        while True:
            sleep(0.5)
            print(num, end=' ')
            if num == fim:
                break
            if inicio < fim:
                if num + passo > fim:
                    break
                num += passo
            elif inicio > fim:
                if num - passo < fim:
                    break
                num -= passo
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
contador(
    int(input('Ínicio: ')),
    int(input('Fim: ')),
    int(input('Passo: '))
)