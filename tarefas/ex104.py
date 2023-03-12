def leiaint(msg):
    while True:
        n = str(input(msg))
        if not n.isnumeric():
            print("\033[31mErro! Digite um número inteiro válido\033[m")
        else:
            break
    return n


n = leiaint('Digite um número: ')
print(f"Você acabou de digitar o número {n}")
