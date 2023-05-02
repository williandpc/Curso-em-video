from time import sleep


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


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(str(txt).center(42))
    print(linha())


def menu(lista):
    cabecalho("MENU PRINCIPAL")
    print()
    for indice, item in enumerate(lista):
        print(f"\033[33m{indice + 1}\033[m - \033[34m{item}\033[m")
    print()
    print(linha())
    opt = leiaint('\033[33mSua Opção: \033[m')
    print()
    return opt


def abrirlist():
    try:
        with open('registro.txt', 'r') as registro:
            print('Registro encontrado e aberto com sucesso!')
            return registro
    except FileNotFoundError:
        with open('registro.txt', 'w') as registro:
            print('Registro, não encontrado! Gerando um novo registro...')
            sleep(1)
            print("Registro gerado com sucesso!")
            return registro
