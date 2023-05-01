def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO: Por favor, digite um número inteiro válido\033[m")
            continue
        except KeyboardInterrupt:
            print("\033[31mEntrada de dados interrompida pelo usuário.\033[m")
            continue
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO: Por favor, digite um número inteiro válido\033[m")
            continue
        except KeyboardInterrupt:
            print("\033[31mEntrada de dados interrompida pelo usuário.\033[m")
            continue
        else:
            return n


num = leiaint('Digite um valor: ')
r = leiafloat("Digite um valor: ")
print(f"O valor inteiro digitado foi {num} e o valor real digitado foi {r} ")
